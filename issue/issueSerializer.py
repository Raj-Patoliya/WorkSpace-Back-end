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
    priority_id = serializers.PrimaryKeyRelatedField(queryset=Priority.objects.all(), source='priority')
    status_id = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all(), source='status')
    assignee_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='assignee')
    reporter_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='reporter')
    project = serializers.StringRelatedField(source='project.name')

    class Meta:
        model = Issue
        fields = ('id', 'issue_summary', 'issue_description', 'priority_id', 'status_id', 'assignee_id', 'reporter_id',
                  'project','issue_type', 'created_date', 'updated_date')
    #
    # def get_project(self,obj):
    #     project = Project.objects.filter(title=obj.project).first()
    #     serializer = ProjectSerializer(data=project)
    #     return serializer
    #
    #
    # def get_issueType(self,obj):
    #     issueType = IssueType.objects.filter(pk=obj.issue_type_id)
    #     return issueType
    #
    #
    # def get_status(self,obj):
    #     status = Status.objects.filter(pk=obj.status_id)
    #     return status
    #
    # def get_priority(self,obj):
    #     priority = Priority.objects.filter(pk=obj.priority_id)
    #     return priority
    #
    # def get_assignee(self,obj):
    #     assignee = User.objects.filter(pk=obj.assignee_id)
    #     return assignee
    #
    # def get_reporter(self,obj):
    #     reporter = User.objects.filter(pk=obj.reporter_id)
    #     return reporter
    # project = serializers.CharField(Project)
    # class Meta:
    #     model = Issue
    #     fields = '__all__'