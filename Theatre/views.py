from django.shortcuts import render, get_object_or_404
from .models import Showtimes, Seats
from Bookings.models import Bookings  # assuming you store booked seats here

def select_seats_view(request, showtime_id):
    showtime = get_object_or_404(Showtimes, id=showtime_id)

    # Get all seats for this showtime's theatre and screen
    all_seats = Seats.objects.filter(
        theatre=showtime.theatre,
        screen_number=showtime.screen_number
    )

    # Create a dictionary to group seats by row
    seat_rows = {}
    for seat in all_seats:
        row = seat.row_label
        if row not in seat_rows:
            seat_rows[row] = []

        # Check if seat is sold
        is_sold = Bookings.objects.filter(showtime=showtime, seats__id=seat.id).exists()

        # Fake bestseller logic (you can replace this with your logic)
        is_bestseller = seat.seat_number in range(5, 10)  # example bestseller range

        seat_obj = {
            'id': seat.id,
            'row': seat.row_label,
            'number': seat.seat_number,
            'is_sold': is_sold,
            'is_bestseller': is_bestseller,
            'display': f"{seat.row_label}{seat.seat_number}"
        }
        seat_rows[row].append(seat_obj)

    context = {
        'showtime': showtime,
        'seat_rows': dict(sorted(seat_rows.items())),  # sort rows A to Z
        'formatted_time': showtime.show_time.strftime('%A, %d %B %Y, %I:%M %p')
    }
    return render(request, 'seating.html', context)
