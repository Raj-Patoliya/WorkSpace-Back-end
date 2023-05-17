from django.contrib import admin
from django.urls import path,include
from .views import UserRegistration,UserProfile,UsersList,CurrentUser,UserIssueBasicDetails
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
urlpatterns = [
    path("create/", UserRegistration.as_view(),name="user"),
    path("profile/", UserProfile.as_view(),name="user"),
    path('login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("avtar/", UserProfile.as_view(),name="avtar"),
    path("list",UsersList.as_view(),name="users_list"),
    path("current-user",CurrentUser.as_view(),name="CurrentUser"),
    path("user-issue",UserIssueBasicDetails.as_view(),name="UserIssueBasicDetails")
]