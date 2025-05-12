from django.shortcuts import render
from Movies.models import Movies
from Accounts.models import User
from Bookings.models import Bookings, BookingSeats
from Payment.models import Payment
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    movies = Movies.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'dashboard/home.html', context)

@login_required
def your_orders(request):
    user = request.user
    bookings = Bookings.objects.filter(user=user, booking_status='confirmed').order_by('-booking_time')
    
    tickets = {}
    for booking in bookings:
        try:
             payment = Payment.objects.filter(booking=booking).latest('transaction_time') 
        except Payment.DoesNotExist:
            payment = None

        tickets[booking.id] = {
            'booking': booking,
            'payment': payment,
            'seats': BookingSeats.objects.filter(booking=booking)
        }

    context = {
        'tickets': tickets,
        'user': user,
    }
    return render(request, 'dashboard/your_orders.html', context)


