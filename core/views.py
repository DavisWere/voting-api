from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny
import requests
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from core.models import(User)

from core.serializers import ( CustomTokenObtainPairSerializer, UserSerializer)

# Create your views here.
class CustomObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = CustomTokenObtainPairSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
