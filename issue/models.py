from django.db import models
from user.models import *
from project.models import *
# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='icons/', blank=True, max_length=1000)

    class Meta:
        db_table = "status"
class Priority(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='icons/', blank=True, max_length=1000)

    class Meta:
        db_table = "priority"
class IssueType(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='icons/', blank=True, max_length=1000)

    class Meta:
        db_table = "issue_type"
class Issue(models.Model):
    issue_summary = models.CharField(max_length=200)
    issue_description = models.TextField()
    priority = models.ForeignKey(Priority,related_name="priority",on_delete=models.CASCADE)
    status = models.ForeignKey(Status,related_name="status",on_delete=models.CASCADE)
    assignee = models.ForeignKey(User,related_name="assignee",on_delete=models.CASCADE)
    reporter = models.ForeignKey(User,related_name="reporter",on_delete=models.CASCADE)
    project = models.ForeignKey(Project,related_name="projects",on_delete=models.CASCADE)
    issue_type = models.ForeignKey(IssueType,related_name="issue_type",on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField()

    class Meta:
        db_table = "issue"
class Comment(models.Model):
    issue_id = models.ForeignKey(Issue,related_name="comment",on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,related_name="commentator",on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)

    class Meta:
        db_table = "comment"
class ActivityLog(models.Model):
    issue_id = models.ForeignKey(Issue, related_name="activityLog", on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
    activityType = models.TextField()
    prev = models.TextField()
    latest = models.TextField()
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)

    class Meta:
        db_table = "activityLog"
class Attachment(models.Model):
    issue_id = models.ForeignKey(Issue, related_name="attachment", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="uploadedBy", on_delete=models.CASCADE)
    attachment_file = models.ImageField(upload_to='attachment/', blank=True, max_length=1000)
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)