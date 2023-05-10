from rest_framework import serializers
from user.serializer import *
from issue.issueSerializer import *
from user.models import User,Role
from project.models import *
from issue.models import *

class AddTeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

    def validate(self, data):
        # This method will validate the entire serializer data
        team = Team.objects.filter(user_id=data['user'], project_id=data["project"]).first()
        if team:
            raise serializers.ValidationError("Member Already Exist")
        return data

class ProjectTeamSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    def get_user(self,obj):
        return User.objects.filter(pk=obj.user_id).values('id','profile','fullName')
    def get_role(self,obj):
        return Role.objects.filter(pk=obj.role_id).values('id','name')

    class Meta:
        model = Team
        fields = '__all__'
class ProjectSerializer(serializers.ModelSerializer):
    team = ProjectTeamSerializer(read_only=True,many=True)
    owner = serializers.SerializerMethodField()

    def get_owner(self,obj):
        user = UserProfileSerializer(obj.created_by)
        return User.objects.filter(pk=user.data["id"]).values('id','profile','fullName')
    class Meta:
        model = Project
        fields = '__all__'
class UserProjectSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(read_only=True,many=True)

    class Meta:
        model = User
        exclude = ["password"]

class AllProjectOfUserSerializer(serializers.ModelSerializer):
    project = serializers.SerializerMethodField()

    def get_project(self,obj):
        projectid = Team.objects.filter(user_id=obj.id).values("project_id")
        project = list()
        for us in projectid:
            data = Project.objects.filter(id=us["project_id"]).all()
            seri = ProjectSerializer(data, many=True)
            project.append(seri.data)
        return project

    class Meta:
        model = User
        fields = '__all__'

class ProjectIssueSerializer(serializers.ModelSerializer):
    # team = ProjectTeamSerializer(read_only=True)
    # issue = serializers.SerializerMethodField()
    project = ProjectSerializer(read_only=True)
    issue_type = IssueTypeSerializer(read_only=True)
    status = StatusSerializer(read_only=True)
    issueType = IssueTypeSerializer(read_only=True)
    assignee = UserListSerializer(read_only=True)
    priority = PrioritySerializer(read_only=True)

    # def get_issue(self,obj):
    #     datas = Issue.objects.filter(project_id=obj.id).values("id","issue_summary","issue_description","reporter","assignee","status","priority","issue_type")
    #     d = list()
    #     for data in datas:
    #         status = Status.objects.filter(pk=int(data["status"])).values("id", "name", "icon")
    #         data["status"] = status
    #
    #         priority = Priority.objects.filter(pk=int(data["priority"])).values("id", "name", "icon")
    #         data["priority"] = priority
    #
    #         issue_type = IssueType.objects.filter(pk=int(data["issue_type"])).values("id", "name", "icon")
    #         # data["issue_type"] = issue_type
    #         serializer = IssueTypeSerializer(data=issue_type)
    #         # if serializer.is_valid():
    #         #     print("------------------",serializer.data)
    #         #     data["issue_type"] = serializer.data
    #         # else:
    #         #     print("------------------")
    #         #     print(serializer.errors)
    #         reporter = User.objects.filter(pk=int(data["reporter"])).values("id", "fullName", "profile")
    #         data["reporter"] = reporter
    #         assignee = User.objects.filter(pk=int(data["assignee"])).values("id", "fullName", "profile")
    #         data["assignee"] = assignee
    #         d.append(data)
    #     return datas

    class Meta:
        model = Issue
        fields = "__all__"
