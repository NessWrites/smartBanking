

# Create  models here.
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from .tracker import AccountNumberTracker

from smart_banking.settings import AUTH_USER_MODEL

class User(AbstractUser):
    email = models.EmailField(max_length=50,unique=True)
    phone = models.CharField(max_length=10, unique = True)
    firstName = models.CharField(max_length=20, null = False, blank=False)
    lastName = models.CharField(max_length=20, null = False, blank=False)
    address = models.CharField(max_length=50, null = False, blank=False)
    district = models.CharField(max_length=50, null = False, blank=False)
    city = models.CharField(max_length=50, null = False, blank=False)
    provinces = models.CharField(max_length=50, null = False, blank=False)
    dateOfBirth = models.CharField(max_length=50, null = False, blank=False)
    panNumber = models.CharField(max_length=50,  unique = True, blank=False)
    createdAt = models.DateTimeField(auto_now_add= True)
    createdBy = models.ForeignKey(AUTH_USER_MODEL, on_delete  = models.CASCADE, related_name = "creator", null=True)
    accountNumber = models.PositiveIntegerField(unique=True, blank=True, null=True)
    
    USERNAME_FIELD = 'phone'
    PASSWOED_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']
    
    def save(self, *args,  **kwargs):
        if not self.accountNumber:
            self.accountNumber = self.generate_account_number()
        super(User, self).save(*args, **kwargs)
    
    def generate_account_number(self):
        
        tracker, created = AccountNumberTracker.objects.get_or_create(id=1)
        tracker.last_account_number += 1
        tracker.save()
        return tracker.last_account_number
        
        

    def __str__(self):
        return self.username
