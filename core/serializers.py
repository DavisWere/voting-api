import os
from datetime import timedelta

import requests
from django.db import transaction
from django.db.models import Sum
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from core.models import *


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser
        return token
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 
                  'password', 'profile_picture', 'user_type']
        

    # remove the password field
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('password')
        return data
    
class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'
    
    
