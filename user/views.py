from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from .serializer import UserProfileSerializer,ProfileSerializer
from .models import *
class UserRegistration(generics.ListCreateAPIView):
    queryset = User.object.all()
    serializer_class = UserProfileSerializer


class UserProfile(generics.ListCreateAPIView):
    queryset = ProfileAvtar.objects.all()
    serializer_class = ProfileSerializer