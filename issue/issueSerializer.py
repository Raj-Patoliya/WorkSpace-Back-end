from rest_framework import serializers
from issue.models import *
from project.models import *
from user.models import *
from project.projectSerializer import *
from user.serializer import *


class IssueTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueType
        fields = "__all__"
class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = "__all__"
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = "__all__"
class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = "__all__"

class IssueSerializer(serializers.ModelSerializer):
    status = StatusSerializer(read_only=True)
    priority = PrioritySerializer(read_only=True)
    issueType = IssueTypeSerializer(read_only=True)
    comment = CommentSerializer(read_only=True,partial=True)
    attachment = AttachmentSerializer(read_only=True,partial=True)
    activityLog = ActivityLogSerializer(read_only=True,partial=True)

    class Meta:
        model = Issue
        fields = "__all__"

class IssueCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('id', 'issue_summary', 'issue_description', 'priority', 'status', 'assignee', 'reporter',
                  'project','issue_type', 'created_date', 'updated_date')
