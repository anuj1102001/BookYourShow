from django.shortcuts import get_object_or_404, render,redirect
from .models import Movies,genres, languages
from Reviews.models import Reviews
from django.db.models import Avg
from django.utils import timezone
# Create your views here.


def Movielist(request):
    language = request.GET.get('language')
    genre = request.GET.get('genre')

    movies = Movies.objects.all()

    if language:
        movies = movies.filter(language=language)
    if genre:
        movies = movies.filter(genre=genre)

    context = {
        'movies': movies,
        'selected_language': language,
        'selected_genre': genre,
        'genres': genres,
        'languages': languages,
    }
    return render(request, 'movies/movies.html', context)


def MovieDetail(request, movie_id):
    movie = Movies.objects.get(movie_id=movie_id)
    return render(request, 'movies/moviedetails.html', {'movie': movie})

def movieview(request, slug):
    if Movies.objects.filter(slug=slug).exists():
        movie = Movies.objects.get(slug=slug)

        # POST request
        if request.method == 'POST':
            if 'delete_review_id' in request.POST:
                # Handle delete request
                review_id = request.POST.get('delete_review_id')
                review_to_delete = get_object_or_404(Reviews, pk=review_id, user=request.user)
                review_to_delete.delete()
                return redirect('moviesview', slug=slug)
            else:
                # Handle add review
                rating = request.POST.get('rating')
                review_text = request.POST.get('review_text')
                if request.user.is_authenticated:
                    if rating and review_text:
                        Reviews.objects.create(
                            user=request.user,
                            movie=movie,
                            rating=rating,
                            review_text=review_text,
                            created_at=timezone.now()
                        )
                        return redirect('moviesview', slug=slug)
                else:
                    return redirect('login')

        review = Reviews.objects.filter(movie=movie)
        no_users = review.count()
        rating = review.aggregate(avg_rating=Avg('rating'))['avg_rating'] if no_users > 0 else None

        context = {
            'movie': movie,
            'rating': rating,
            'no_users': no_users,
            'review': review
        }
        return render(request, 'movies/moviedetails.html', context)
    
    return render(request, 'movies/404.html', status=404)

# filter movies 
def filtered_movies_view(request):
    language = request.GET.get('language')
    genre = request.GET.get('genre')

    movies = Movies.objects.all()

    if language:
        movies = movies.filter(language=language)
    if genre:
        movies = movies.filter(genre=genre)

    context = {
        'movies': movies,
        'selected_language': language,
        'selected_genre': genre,
        'genres': genres,
        'languages': languages,

    }
    return render(request, 'movies/filter.html', context)

