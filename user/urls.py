from django.contrib import admin
from django.urls import path,include
from .views import UserRegistration,UserProfile

urlpatterns = [
    path("create/", UserRegistration.as_view(),name="user"),
    path("avtar/", UserProfile.as_view(),name="avtar"),
]
