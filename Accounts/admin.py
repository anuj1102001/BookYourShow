from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ['first_name', 'last_name', 'email', 'phone', 'is_theatre_manager', 'is_approved', 'otp','otp_verified']