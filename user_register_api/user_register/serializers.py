

from django.contrib.auth.models import User
from rest_framework import serializers

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
