from rest_framework import serializers
from user.serializer import *
from issue.issueSerializer import *
from user.models import User,Role
from project.models import *
from issue.models import *

class ProjectTeamSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()

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
        print(user.data)
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
    team = ProjectTeamSerializer(many=True)
    issue = serializers.SerializerMethodField()

    def get_issue(self,obj):
        data = Issue.objects.filter(project_id=obj.id).values("id","issue_summary","issue_description","reporter","assignee","status","priority","issue_type")
        return data

    class Meta:
        model = Project
        fields = ['team',"issue"]
