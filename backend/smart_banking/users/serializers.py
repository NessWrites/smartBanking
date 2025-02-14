from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName',
                  'address', 'district','city',
                  'provinces', 'dateOfBirth', 'panNumber',
                  'email','phone','username', 'password','accountNumber']
        extra_kwargs = {'password': {'write_only': True}}

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['firstName', 'lastName',
                  'address', 'district', 'city',
                  'provinces', 'dateOfBirth', 'panNumber',
                  'email', 'phone', 'username', 'password', 'accountNumber']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):  # Correct indentation
        password = validated_data.pop('password')  # Extract password
        user = User(**validated_data)  # Create user instance without password
        user.set_password(password)  # Hash the password
        user.save()  # Save the user
        return user