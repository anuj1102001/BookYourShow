from django.contrib import admin
from .models import Bookings, BookingSeats

@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'showtime', 'booking_time', 'total_amount', 'booking_status']

@admin.register(BookingSeats)
class BookingSeatsAdmin(admin.ModelAdmin):
    list_display = ['id', 'booking', 'seat']
