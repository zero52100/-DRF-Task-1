

from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=10)

    def validate_password(self, value):
        
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")
        if not any(char.islower() for char in value):
            raise serializers.ValidationError("Password must contain at least one lowercase letter.")
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Password must contain at least one digit.")
        special_characters = "!@#$%^&*()-+"
        if not any(char in special_characters for char in value):
            raise serializers.ValidationError("Password must contain at least one special character.")
        return value

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])

        if user:
            refresh = RefreshToken.for_user(user)
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user
            }
        else:
            raise serializers.ValidationError("Invalid credentials")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')