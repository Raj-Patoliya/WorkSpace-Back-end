from django.contrib import admin
from django.urls import path,include
from project.views import UserProjectCRUD,AllProjectForUser
urlpatterns = [
    path("create/", UserProjectCRUD.as_view(), name="project"),
    path("all-list/", AllProjectForUser.as_view(), name="all project"),
]
