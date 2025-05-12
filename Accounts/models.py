from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.IntegerField(unique=True,null=True,blank=True)
    is_theatre_manager = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    otp_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'  
    REQUIRED_FIELDS = []  
