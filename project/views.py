from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView,Response
from rest_framework.permissions import IsAuthenticated
from project.models import Project, Team
from user.models import User,Role
from project.projectSerializer import ProjectIssueSerializer, ProjectSerializer,ProjectTeamSerializer,UserProjectSerializer
from django.http import Http404
from issue.issueSerializer import *

class UserProjectCRUD(APIView):
    # permission_classes = [IsAuthenticated]
    # def get_object(self, pk):
    #     try:
    #         return User.objects.filter(pk=pk).get()
    #     except Project.DoesNotExist:
    #         raise Http404

    def get(self,request,keys):
        project = Project.objects.filter(key=keys).first()
        serializer = ProjectSerializer(project, read_only=True)
        return Response(serializer.data)

    def post(self,request):
        project = Project()
        project.title = request.data['title']
        project.key = request.data['key']
        project.description = request.data['description']
        project.created_by = request.user
        project.save()
        lastCreatedProject = Project.objects.order_by('-start_date').first()

        role = Role.objects.order_by('id').first()
        team = Team()
        team.user = request.user
        team.project = lastCreatedProject
        team.role = role
        team.save()
        return Response({"data": "Hakuna Matata"})

    def put(self,request,pid):
        project = Project.objects.filter(pk=pid)
        serializer = ProjectSerializer(project,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AllProjectForUser(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.filter(pk=pk).get()
        except Project.DoesNotExist:
            raise Http404

    def get(self,request):
        user = self.get_object(pk=request.user.id)
        res = dict()
        serializer = UserProjectSerializer(user)
        projectid = Team.objects.filter(user_id=request.user.id).values("project_id")
        project = list()
        for us in projectid:
            data = Project.objects.filter(id=us["project_id"]).all()
            seri = ProjectSerializer(data, many=True)
            project.append(seri.data[0])
        res["projects"] = project
        res["id"] = serializer.data["id"]
        res["fullName"] = serializer.data["fullName"]
        res["email"] = serializer.data["email"]
        res["profile"] = serializer.data["profile"]
        res["is_verified"] = serializer.data["is_verified"]
        res["is_active"] = serializer.data["is_active"]
        res["is_staff"] = serializer.data["is_staff"]
        res["is_superuser"] = serializer.data["is_superuser"]
        res["last_login"] = serializer.data["last_login"]
        res["created_at"] = serializer.data["created_at"]
        res["updated_at"] = serializer.data["updated_at"]
        return Response({"data":res})

class ProjectIssueView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,keys):
        serializer = ProjectIssueSerializer(Issue.objects.filter(project__key=keys), many=True)
        # project = Project.objects.filter(key=keys).first()
        # serializer = ProjectIssueSerializer(Issue.objects.all(),many=True)
        print(serializer.data)
        return Response({"data":serializer.data})

