from django.shortcuts import redirect, render
from Movies.models import Movies
import Reviews

def add_review(request,slug):
    user = user.objects.get(username=request.user)
    movie = Movies.objects.get(slug=slug)
    if request.method == 'POST':
        rating = request.POST['review_text']
        review_text = request.POST['review_text']
        Reviews.objects.create(user=user,movie=movie,
                               rating=rating,review_text=review_text)
        return redirect(f'/movie/{slug}/')
    return render(request,'add_review.html')