from django.db import models
from Accounts.models import User
from Movies.models import Movies
from django.utils import timezone

# Create your models here.

class Theatres(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=2000)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.city}"


class Showtimes(models.Model):
    start_time = models.DateTimeField()
    movie = models.ForeignKey(Movies, on_delete=models.SET_NULL, null=True)
    theatre = models.ForeignKey(Theatres, on_delete=models.CASCADE)
    show_time = models.DateTimeField()
    screen_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.movie} at {self.theatre.name} - Screen {self.screen_number} on {self.show_time.strftime('%d %b %Y %I:%M %p')}"


class Seats(models.Model):
    theatre = models.ForeignKey(Theatres, on_delete=models.CASCADE)
    screen_number = models.IntegerField(null=True, blank=True)
    row_label = models.CharField(max_length=10)
    seat_number = models.IntegerField()
    seat_type = models.CharField(max_length=20, choices=[['gold', 'Gold'], ['silver', 'Silver'],['luxury','Luxury']])

    def __str__(self):
        return f"{self.theatre.name} - Screen {self.screen_number} - {self.row_label}{self.seat_number} ({self.seat_type.title()})"
