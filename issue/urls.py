from django.contrib import admin
from django.urls import path,include
from issue.views import *
from issue.views import IssueTypeCRUDVIEW
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("issue-type",IssueTypeCRUDVIEW.as_view(),name="issue-type"),
    path("issue-priority",PriorityCRUDVIEW.as_view(),name="issue-priority"),
    path("issue-status",StatusCRUDVIEW.as_view(),name="issue-status"),
    path("issue-comment",CommentCRUDVIEW.as_view(),name="issue-comment"),
    path("issue-attachment",AttachmentCRUDVIEW.as_view(),name="issue-attachment"),
    path("issue-activityLog",ActivityLogCRUDVIEW.as_view(),name="issue-activityLog"),
    path("issues",IssueCRUDVIEW.as_view(),name="issues"),
    path("issue-update/<int:issue_id>",UpdateIssueFields.as_view(),name="issues"),
    path("issue-comment/<int:issue_id>",PostCommentIssue().as_view(),name="comment")
]
