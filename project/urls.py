from django.contrib import admin
from django.urls import path,include
from project.views import UserProjectCRUD,AllProjectForUser,ProjectIssueView,TeamCrudView
urlpatterns = [
    path("CRUD/", UserProjectCRUD.as_view(), name="project-CRUD"),
    path("CRUD/<str:keys>", UserProjectCRUD.as_view(), name="project-CRUD-keys"),
    path("team/", TeamCrudView.as_view(), name="project-add-team"),
    path("team/<str:keys>", TeamCrudView.as_view(), name="project-team"),
    path("all-list/", AllProjectForUser.as_view(), name="all-project"),
    path("work/<str:keys>",ProjectIssueView.as_view(),name="project-issue")
]



