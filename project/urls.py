from django.contrib import admin
from django.urls import path,include
from project.views import ProjectCRUDView
urlpatterns = [
    path("list/", ProjectCRUDView.as_view(), name="project"),
]
