from django.db import models
from Accounts.models import User
from Movies.models import Movies
# Create your models here.

class Reviews(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE,related_name="reviews")
    rating = models.IntegerField()
    review_text = models.TextField()
    created_at = models.DateField(auto_now_add=True)