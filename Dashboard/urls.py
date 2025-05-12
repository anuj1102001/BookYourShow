from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('your-orders/', views.your_orders, name='your_orders'),

]
