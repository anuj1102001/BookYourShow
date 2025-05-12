from django.db import models
from Accounts.models import User
from Theatre.models import Showtimes,Seats,Theatres
# Create your models here.

class Bookings(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtimes,on_delete=models.SET_NULL,null=True,blank=True)
    booking_time = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)
    booking_status = models.CharField(max_length=20,choices=[['confirmed','Confirmed'],['cancelled','Cancelled'],['pending','Pending']])

class BookingSeats(models.Model):
    booking = models.ForeignKey(Bookings,on_delete=models.CASCADE)
    seat = models.ForeignKey(Seats,on_delete=models.SET_NULL,null=True,blank=True)