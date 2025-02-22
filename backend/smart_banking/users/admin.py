from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, AccountType, Transaction, TransactionType

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('id', 'username', 'firstName', 'lastName', 'email', 'phone', 'accountNumber', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'phone', 'accountNumber')
    ordering = ('id',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('firstName', 'lastName', 'email', 'phone', 'dateOfBirth', 'panNumber', 'address', 'district', 'city', 'province')}),
        ('Account Details', {'fields': ('accountNumber', 'createdBy', 'is_staff', 'is_active')}),
        ('Permissions', {'fields': ('groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )


class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'transaction_type', 'amount', 'date')
    search_fields = ('user__username', 'transaction_type__name', 'amount')
    ordering = ('-date',)

class TransactionTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

# Register models
admin.site.register(User, CustomUserAdmin)
admin.site.register(AccountType, AccountTypeAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(TransactionType, TransactionTypeAdmin)
