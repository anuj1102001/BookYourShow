from django.contrib import admin
from .models import Theatres,Showtimes,Seats
# Register your models here.

@admin.register(Theatres)
class TheatresAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','address','manager']
    
@admin.register(Showtimes)
class ShowtimesAdmin(admin.ModelAdmin):
    list_display = ['id','movie', 'theatre', 'show_time', 'screen_number']

@admin.register(Seats)
class SeatsAdmin(admin.ModelAdmin):
    list_display = ['id', 'theatre', 'screen_number', 'row_label', 'seat_number', 'seat_type']