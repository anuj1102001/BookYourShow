from pyexpat.errors import messages
from django.contrib import messages
from django.conf import settings
from Payment.models import Payment
import stripe  # type: ignore
import json
from django.shortcuts import redirect, render,HttpResponse,get_object_or_404
from Theatre.models import Theatres,Seats,Showtimes
from .models import Showtimes, Bookings, Seats, BookingSeats
from Accounts.models import User
from Movies.models import Movies
from datetime import datetime,timedelta
from django.utils import timezone  # ✅ This has timezone.now()
from django.utils.dateformat import format
from django.contrib.auth.decorators import login_required


stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def Theatre_show_time(request, slug):
    today = datetime.today().date()
    selected_date_str = request.GET.get('date')
    if selected_date_str:
        selected_date = datetime.strptime(selected_date_str, "%B %d, %Y").date()
    else:
        selected_date = today
    start_date = today
    week = []
    for i in range(7):
        day = start_date + timedelta(days=i)
        week.append({
            'name': day.strftime("%a").upper(),
            'day': day.day,
            'month': day.strftime("%b").upper(),
            'date': day
        })

    if Movies.objects.filter(slug=slug).exists():
        movie = Movies.objects.get(slug=slug)
        theater_showtimes = [
            Showtimes.objects.filter(movie=movie, theatre=theatre, show_time__date=selected_date).order_by('show_time')
            for theatre in Theatres.objects.all()
            if Showtimes.objects.filter(movie=movie, theatre=theatre, show_time__date=selected_date).exists()
        ]

        # Debugging output to check showtimes and their IDs
        for showtime_list in theater_showtimes:
            for show in showtime_list:
                print(f"Showtime ID: {show.id}, Movie: {show.movie.title}, Theatre: {show.theatre.name}")

        context = {
            'theater_showtimes': theater_showtimes, 
            'week': week,
            'today': today,
            'selected_date': selected_date
        }
        return render(request, 'theatre/theatre.html', context)

    return render(request, 'movies/404.html')



def seat_selection_view(request, showtime_id):
    showtime = Showtimes.objects.get(id=showtime_id)
    all_seats = Seats.objects.filter(
        theatre=showtime.theatre,
        screen_number=showtime.screen_number
    ).order_by('row_label', 'seat_number')

    seat_rows = {
        'A': list(range(1, 25)), 'B': list(range(1, 25)),
        'C': list(range(1, 25)), 'D': list(range(1, 25)), 'E': list(range(1, 25)), 'F': list(range(1, 25)),
        'G': list(range(1, 25)), 'H': list(range(1, 25)), 'I': list(range(1, 25)), 'J': list(range(1, 25)),
        'K': list(range(1, 25)), 'L': list(range(1, 25)), 'M': list(range(1, 25)),
        'N': list(range(1, 25)), 'O': list(range(1, 25)), 'P': list(range(1, 25)),
        'Q': list(range(1, 25)), 'R': list(range(1, 25)),
    }

    for seat in all_seats:
        row = seat.row_label
        if row not in seat_rows:
            seat_rows[row] = []
        seat_rows[row].append(seat)

    formatted_time = showtime.start_time.strftime('%I:%M %p') if showtime.start_time else "Not Set"

    context = {
        'showtime': showtime,
        'seat_rows': seat_rows,
        'formatted_time': formatted_time,
    }

    return render(request, 'theatre/seating.html', context)



@login_required(login_url='login')
def book_ticket_view(request, showtime_id):
    if request.method == 'POST':
        selected_seats_json = request.POST.get('selected_seats')
        total_amount = request.POST.get('total_amount')

        if not selected_seats_json or not total_amount:
            return HttpResponse("Missing seat data or amount.", status=400)

        try:
            selected_seats_data = json.loads(selected_seats_json)
        except json.JSONDecodeError:
            return HttpResponse("Invalid seat data format.", status=400)

        showtime = get_object_or_404(Showtimes, id=showtime_id)

        # Create a booking
        booking = Bookings.objects.create(
            user=request.user,
            showtime=showtime,
            total_amount=total_amount,
            booking_status='confirmed'
        )

        # Add seats to the booking
        for seat in selected_seats_data:
            seat_id = seat.get('id')
            if not seat_id or not str(seat_id).isdigit():
                print("Invalid seat ID:", seat_id)
                continue  # Skip if blank or invalid

            try:
                seat_obj = Seats.objects.get(id=seat_id)
                BookingSeats.objects.create(booking=booking, seat=seat_obj)
            except Seats.DoesNotExist:
                print(f"Seat with id {seat_id} does not exist.")
                continue

        # Pass the relevant context for rendering
        return render(request, 'payment/proceedpayment.html', {
            'showtime': showtime,
            'user': request.user, 
            'ticket': [seat['number'] for seat in selected_seats_data],  
            'total_amount': total_amount,
            'convenience_fee': 20, 
            'sub_total': float(total_amount) + 20,
            'stripe_public_key':settings.STRIPE_PUBLIC_KEY, 
            'booking': booking
        })

    return HttpResponse("Invalid request method.", status=405)

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Bookings, id=booking_id, user=request.user)
    
    # Check if showtime is today or tomorrow
    show_date = booking.showtime.start_time.date()
    today = timezone.now().date()
    tomorrow = today + timezone.timedelta(days=1)

    if show_date < today or show_date > tomorrow:
        messages.error(request, "Cancellation is only allowed for today's or tomorrow’s bookings.")
        return redirect('your_orders')

    # Cancel logic
    booking.booking_status = 'cancelled'
    booking.save()

    # Free up the seats
    BookingSeats.objects.filter(booking=booking).delete()

    # Optional: log a refund (already exists)
    Payment.objects.create(
        booking=booking,
        payment_method='card',
        amount=booking.total_amount,
        status='refunded'
    )

    messages.success(request, "Booking cancelled successfully and amount has been refunded successfully.")
    return redirect('your_orders')
