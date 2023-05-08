from django.contrib import admin
from django.urls import path,include
from project.views import UserProjectCRUD,AllProjectForUser,ProjectIssueView
urlpatterns = [
    path("CRUD/", UserProjectCRUD.as_view(), name="project"),
    path("CRUD/<str:keys>", UserProjectCRUD.as_view(), name="project"),
    path("all-list/", AllProjectForUser.as_view(), name="all project"),
    path("work/<str:keys>",ProjectIssueView.as_view(),name="project-issue")
]
