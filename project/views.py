from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from project.models import Project, Team
from user.models import User
from project.projectSerializer import ProjectSerializer
from django.http import Http404


class ProjectCRUDView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(cls, self, user_id):
        try:
            return Project.objects.filter(user_id=user_id).values()
        except Project.DoesNotExist:
            raise Http404

    def get(self,request):
        if Project.objects.filter(Project.created_by == request.user.id).exists():
            return Project.objects.filter(Project.created_by == request.user.id)
