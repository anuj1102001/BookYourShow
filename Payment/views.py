from django.shortcuts import get_object_or_404, render, redirect
from Bookings.models import BookingSeats, Bookings
from django.conf import settings
from Payment.models import Payment
import stripe  # type: ignore

stripe.api_key = settings.STRIPE_SECRET_KEY

def payment_page(request, booking_id):
    booking = Bookings.objects.get(id=booking_id)

    if request.method == 'POST':
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'inr',
                    'product_data': {
                        'name': 'Ticket Booking',
                    },
                    'unit_amount': int((booking.total_amount+20)*100),
                },
                'quantity': 1,
            }],
            mode='payment',
            billing_address_collection='required',
            success_url=f'http://127.0.0.1:8000/payment/success/{booking_id}/',
            cancel_url=f'http://127.0.0.1:8000/payment/cancel/{booking_id}/',
        )
        return redirect(session.url, code=303)

    return render(request, 'proceedpayment.html', {'stripe_public_key':settings.STRIPE_PUBLIC_KEY,'booking':booking})



def success(request, booking_id):
    booking = get_object_or_404(Bookings, id=booking_id)
    booking.booking_status = 'confirmed'
    booking.save()
    selected_seats = BookingSeats.objects.filter(booking=booking)
    seat_numbers = [seat.seat.seat_number for seat in selected_seats]
    showtime = booking.showtime

    payment = Payment.objects.create(
        booking=booking,
        payment_method='card',
        amount=booking.total_amount,
        status='success'
    )
    return render(request, 'payment/success.html', {
        'showtime': showtime,
        'booking': booking,
        'selected_seats': seat_numbers,
        'payment': payment
    })

def cancel(request,booking_id):
     booking = Bookings.objects.get(id=booking_id)
     booking.booking_status = 'cancelled'
     booking.save()
     Payment.objects.create(booking=booking,payment_method='card',
                            amount=booking.total_amount,status='failed')
     return render(request, 'payment/cancel.html')