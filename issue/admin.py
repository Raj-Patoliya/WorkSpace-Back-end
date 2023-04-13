from django.contrib import admin
from issue.models import *
@admin.register(Issue)
class Issue(admin.ModelAdmin):
    list_display = ["id",'issue_summary','project_id',
                    'issue_key','issue_description','priority','status','assignee','reporter',
                    'due_date','issue_type','created_date','updated_date']
@admin.register(IssueType)
class IssueType(admin.ModelAdmin):
    list_display = ['id','name','icon']
@admin.register(Priority)
class Priority(admin.ModelAdmin):
    list_display = ['id','name','icon']
@admin.register(Status)
class Status(admin.ModelAdmin):
    list_display = ['id','name','icon']
@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ['id','issue_id','user_id','text','created_date']
@admin.register(ActivityLog)
class ActivityLog(admin.ModelAdmin):
    list_display = ['id','issue_id','user_id','activityType','prev','latest','created_date']
@admin.register(Attachment)
class Attachment(admin.ModelAdmin):
    list_display = []

