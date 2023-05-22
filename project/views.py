from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView,Response
from rest_framework.permissions import IsAuthenticated
from project.models import Project, Team
from user.models import User,Role
from project.projectSerializer import *
from django.http import Http404
from issue.issueSerializer import *
from rest_framework.pagination import LimitOffsetPagination
from django.db.models import Q


class MyCustomPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 100
class UserProjectCRUD(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,keys):
        project = Project.objects.filter(key=keys).first()
        serializer = ProjectSerializer(project, read_only=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self,request):
        # project = Project()
        data = {
            "title":request.data['title'],
            "key":request.data['key'],
            "description":request.data['description'],
            "created_by":request.user.id
        }
        # project.save()
        serializer = CreateProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            lastCreatedProject = Project.objects.order_by('-start_date').first()
            role = Role.objects.order_by('id').first()
            team = Team()
            team.user = request.user
            team.project = lastCreatedProject
            team.role = role
            team.save()
            return Response({"success": "Project Created successfully"},status=status.HTTP_200_OK)
        else:
            return Response({"errors": serializer.errors["non_field_errors"]})


    def put(self,request,pid):
        project = Project.objects.filter(pk=pid)
        serializer = ProjectSerializer(project,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AllProjectForUser(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = MyCustomPagination

    def get(self,request):
        projectId = Team.objects.filter(user_id=request.user.id).values_list("project_id")
        project = Project.objects.filter(id__in=projectId)

        paginator = self.pagination_class()
        paginated_projects = paginator.paginate_queryset(project, request)

        data = ProjectSerializer(paginated_projects, many=True).data
        return paginator.get_paginated_response(data)

class CustomProjectForUser(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = MyCustomPagination

    def post(self,request):
        print(request.data["searchText"])
        projectId = Team.objects.filter(user_id=request.user.id).values_list("project_id")
        project = Project.objects.filter(Q(id__in=projectId) & Q(key__icontains=request.data["searchText"]) |
                                         Q(title__icontains=request.data["searchText"]))

        paginator = self.pagination_class()
        paginated_projects = paginator.paginate_queryset(project, request)

        data = ProjectSerializer(paginated_projects, many=True).data
        return paginator.get_paginated_response(data)

class ProjectIssueView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,keys):
        serializer = ProjectIssueSerializer(Issue.objects.filter(project__key=keys), many=True)
        return Response({"data":serializer.data})

class TeamCrudView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,keys):
        serializer = ProjectTeamSerializer(Team.objects.filter(project__key=keys), many=True)
        return Response({"data":serializer.data})

    def post(self,request):
        data = {
            "project":int(request.data["project"]),
            "role":int(request.data["role"]),
            "user":int(request.data["user"]),
        }
        serializer = AddTeamMemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data},status=status.HTTP_200_OK)
        return Response({"Error": serializer.errors},status=status.HTTP_500_INTERNAL_SERVER_ERROR)