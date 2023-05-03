from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from issue.issueSerializer import *
from issue.models import *
from rest_framework.views import Response
# Create your views here.
class IssueTypeCRUDVIEW(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = IssueType.objects.all()
    serializer_class = IssueTypeSerializer
class PriorityCRUDVIEW(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
class StatusCRUDVIEW(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
class CommentCRUDVIEW(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
class AttachmentCRUDVIEW(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
class ActivityLogCRUDVIEW(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer
class IssueCRUDVIEW(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def post(self,request):
        # issue.project = request.data["project"],
        # issue.issueType = request.data["issueType"],
        # issue.description = request.data["description"],
        # issue.status = request.data["status"],
        # issue.priority = request.data["priority"],
        # issue.summary = request.data["summary"],
        # issue.assignee = request.data["assignee"],
        # issue.reporter = request.data["reporter"],
        # issue.save()
        data = {
            "project": request.data["project"],
            "issueType": request.data["issueType"],
            "description": request.data["description"],
            "status": request.data["status"],
            "priority": request.data["priority"],
            "summary": request.data["summary"],
            "assignee": request.data["assignee"],
            "reporter": request.data["reporter"],
        }
        serializer = IssueCRUDSerializer(data)
        print(serializer)
        if True:
            print("shshs")
            issue = Issue.objects.create(**data)
            print(issue)
            issue.save()
            return Response({"error": serializer.data})
        return Response({"error": "Something Went Wrong"})
