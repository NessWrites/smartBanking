

# Create  models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True, blank=True, null = True)
    phone = models.CharField(max_length=10, unique=True)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']
    

    def __str__(self):
        return self.username
