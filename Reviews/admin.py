from django.contrib import admin
from .models import Reviews

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['review_id', 'user', 'movie', 'rating', 'review_text','created_at'] 