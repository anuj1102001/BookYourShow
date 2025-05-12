from django.urls import path
from . import views

urlpatterns=[
    path('success/<int:booking_id>/',views.success,name='success'),
    path('cancel/<int:booking_id>/',views.cancel,name='cancel'),
    path('payment/<int:booking_id>/', views.payment_page, name='payment'),

]
