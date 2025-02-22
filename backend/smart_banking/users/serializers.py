from rest_framework import serializers
from .models import User, AccountType, Transaction, TransactionType

class AccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountType
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
 

    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName', 'address', 'district', 'city', 'province',
                  'dateOfBirth', 'panNumber', 'email', 'phone', 'username', 'accountNumber']
        extra_kwargs = {'password': {'write_only': True}}

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = '__all__'