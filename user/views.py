from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView,Response
from rest_framework import generics
from .serializer import UserProfileSerializer,ProfileSerializer
from .models import *
class UserRegistration(APIView):
    def post(self, request):
        user = User()
        user.email = request.data["email"]

        user.profile = request.data["profile"]
        user.fullName = request.data["fullName"]
        try:
            user.set_password(request.data["password"])
            user.save()
            return Response({"success": "hakuna matata"})
        except Exception:
            print(Exception)
            return Response({"error": "Something Went Wrong"})


class UserProfile(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProfileAvtar.objects.all()
    serializer_class = ProfileSerializer