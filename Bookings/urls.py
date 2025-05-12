from django.urls import path
from . import views

urlpatterns = [
    path('movie/<slug:slug>/', views.Theatre_show_time, name='select_showtime'),
    path('seat-selection/<int:showtime_id>/', views.seat_selection_view, name='seat_selection'),
    path('book-ticket/<int:showtime_id>/',views.book_ticket_view,name='book_ticket'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),

]