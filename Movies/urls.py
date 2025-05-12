from django.urls import path
from . import views

urlpatterns=[
    path('movie/',views.Movielist,name='movies'),
    path('movie/<int:movie_id>/', views.MovieDetail, name='moviedetails'),
    path('movies/<slug:slug>/',views.movieview, name='moviesview'),
    path('filter/', views.filtered_movies_view, name='filtered_movies'),
    
]