from rest_framework import serializers
from issue.models import *
from project.models import Project,Team
from user.models import User

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

class CreateCommentatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
class CommentSerializer(serializers.ModelSerializer):
    commentator = serializers.SerializerMethodField()

    def get_commentator(self, obj):
        print(obj.user_id)
        return User.objects.filter(email=obj.user_id).values('id', 'profile', 'fullName')

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


class ProjectTeamSerializer(serializers.ModelSerializer):
    # role = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    def get_user(self,obj):
        return User.objects.filter(pk=obj.user_id).values('id','profile','fullName').first()

    # def get_role(self,obj):
    #     return Role.objects.filter(pk=obj.role_id).values('id','name')

    class Meta:
        model = Team
        fields = '__all__'

class IssueSerializer(serializers.ModelSerializer):
    project = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()
    assignee = serializers.SerializerMethodField()
    reporter = serializers.SerializerMethodField()
    status = StatusSerializer(read_only=True)
    priority = PrioritySerializer(read_only=True)
    issue_type = IssueTypeSerializer(read_only=True)
    comment = CommentSerializer(read_only=True,partial=True,many=True)
    attachment = AttachmentSerializer(partial=True,many=True)
    activityLog = ActivityLogSerializer(read_only=True,partial=True,many=True)

    def get_project(self,obj):
        project = Project.objects.filter(pk=obj.project_id).values("id","title","key")
        return project

    def get_team(self,obj):
        serializer = ProjectTeamSerializer(Team.objects.filter(project__id=obj.project_id), many=True)
        return serializer.data

    def get_assignee(self,obj):
        assignee = User.objects.filter(email=obj.assignee).values('id','profile','fullName')
        return assignee

    def get_reporter(self,obj):
        reporter = User.objects.filter(email=obj.reporter).values('id','profile','fullName')
        return reporter
    class Meta:
        model = Issue
        fields = "__all__"

class IssueCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('id', 'issue_summary', 'issue_description', 'priority', 'status', 'assignee', 'reporter',
                  'project','issue_type', 'created_date', 'updated_date',"index")


class IssueBasicDetails(serializers.ModelSerializer):
    issue_type = serializers.SerializerMethodField()
    project = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    def get_issue_type(self,obj):
        issue_type = IssueType.objects.filter(pk=obj.issue_type.id).values("id","name","icon").first()
        return issue_type

    def get_project(self,obj):
        project = Project.objects.filter(pk=obj.project.id).values("id","key","title").first()
        return project

    def get_status(self,obj):
        issue_status = Status.objects.filter(pk=obj.status.id).values("id","name","icon").first()
        return issue_status

    class Meta:
        model = Issue
        exclude = ["issue_description","index","created_date","reporter","assignee","priority"]
class GroupViseIssueSerializer(serializers.ModelSerializer):
    assignedIssue = serializers.SerializerMethodField()
    reportedIssue = serializers.SerializerMethodField()

    def get_assignedIssue(self,obj):
        issue = IssueBasicDetails(Issue.objects.filter(assignee=obj.id),many=True)
        return issue.data

    def get_reportedIssue(self,obj):
        issue = IssueBasicDetails(Issue.objects.filter(reporter=obj.id),many=True)
        return issue.data

    class Meta:
        model = User
        exclude = ["password","user_permissions","last_login","is_active","is_staff","is_superuser","groups","is_verified"]