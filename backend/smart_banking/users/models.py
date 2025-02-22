from django.contrib.auth.models import AbstractUser
from django.db import models
from .tracker import AccountNumberTracker
from smart_banking.settings import AUTH_USER_MODEL

class User(AbstractUser):
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=14, unique=True)
    firstName = models.CharField(max_length=20, null=False, blank=False)
    lastName = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=50, null=False, blank=False)
    district = models.CharField(max_length=50, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    province = models.CharField(max_length=50, null=False, blank=False)
    dateOfBirth = models.CharField(max_length=50, null=False, blank=False)
    panNumber = models.CharField(max_length=50, unique=True, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="creator", null=True)
    accountNumber = models.PositiveIntegerField(unique=True, blank=True, null=True)
    account_balance = models.DecimalField(max_digits=15, decimal_places=2, default=500.00)  # Add balance field
    
    USERNAME_FIELD = 'phone'
    PASSWORD_FIELD = 'phone'  # Fixed typo here
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
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

class AccountType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    

class TransactionType(models.Model):
    DEPOSIT = 'deposit'
    WITHDRAWAL = 'withdrawal'
    TRANSACTION_TYPES = [
        (DEPOSIT, 'Deposit'),
        (WITHDRAWAL, 'Withdrawal'),
    ]
    name = models.CharField(max_length=50, unique=True, choices=TRANSACTION_TYPES)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.transaction_type.name} - {self.amount}"

    def save(self, *args, **kwargs):
        if self.transaction_type.name == TransactionType.DEPOSIT:
            self.user.account_balance += self.amount
        elif self.transaction_type.name == TransactionType.WITHDRAWAL:
            self.user.account_balance -= self.amount
        self.user.save()
        super(Transaction, self).save(*args, **kwargs)
