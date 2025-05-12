from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.registerview,name='register'),
    path('home/',views.home,name='home'),
    path('signin/',views.LoginView,name='signin'),
    path('logout/', views.logoutview, name='logout'),
]