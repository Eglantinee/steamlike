from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password as passwd


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        print(validated_data)
        return User.objects.create_user(**validated_data)

    def validate_password(self, value):
        return passwd(value)

    class Meta:
        model = User
        fields = ('username', 'password',)
