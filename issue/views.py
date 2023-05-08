from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from issue.issueSerializer import *
from issue.models import *
from rest_framework.views import Response
import datetime

# Create your views here.
class IssueTypeCRUDVIEW(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = IssueType.objects.all()
    serializer_class = IssueTypeSerializer
class PriorityCRUDVIEW(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
class StatusCRUDVIEW(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
class CommentCRUDVIEW(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
class AttachmentCRUDVIEW(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
class ActivityLogCRUDVIEW(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer
class IssueCRUDVIEW(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = IssueSerializer

    def post(self,request):
        project = Project.objects.filter(title=request.data["project"]).values("id").first()
        data = {
            "project": project["id"],
            "issue_type": int(request.data["issueType"]),
            "issue_description": request.data["description"],
            "status": int(request.data["status"]),
            "priority": int(request.data["priority"]),
            "issue_summary": request.data["summary"],
            "assignee": int(request.data["assignee"]),
            "reporter": int(request.data["reporter"]),
            "updated_date": datetime.datetime.now()
        }
        serializer = IssueCRUDSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            lastCreatedIssue = Issue.objects.order_by('-created_date').values("id").first()
            attachments = list(request.FILES.values())
            for file in attachments:
                print(file)
                data = {
                    "issue_id": lastCreatedIssue["id"],
                    "attachment_file":file
                }
                serializer = AttachmentSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)
            return Response({"msg": serializer.data})
        else:
            print(serializer.errors)


class UpdateIssueFields(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, issue_id):
        try:
            issue = Issue.objects.get(pk=issue_id)
        except Issue.DoesNotExist:
            return Response({"error": "Issue not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.data["field"] == 'status':
            try:
                status_obj = Status.objects.get(pk=int(request.data["value"]))
                print(status_obj)
            except Status.DoesNotExist:
                return Response({"error": "Status not found."}, status=status.HTTP_404_NOT_FOUND)

            issue.status = status_obj
            print(issue.status)

        elif request.data["field"] == 'priority_id':
            try:
                priority_obj = Priority.objects.get(pk=int(request.data["value"]))
            except Priority.DoesNotExist:
                return Response({"error": "Priority not found."}, status=status.HTTP_404_NOT_FOUND)

            issue.priority = priority_obj

        elif request.data["field"] == 'assignee_id':
            try:
                assignee_obj = User.objects.get(pk=int(request.data["value"]))
            except User.DoesNotExist:
                return Response({"error": "Assignee not found."}, status=status.HTTP_404_NOT_FOUND)

            issue.assignee = assignee_obj

        elif request.data["field"] == 'reporter_id':
            try:
                reporter_obj = User.objects.get(pk=int(request.data["value"]))
            except User.DoesNotExist:
                return Response({"error": "Reporter not found."}, status=status.HTTP_404_NOT_FOUND)

            issue.reporter = reporter_obj

        elif request.data["field"] == 'issue_type_id':
            try:
                issue_type_obj = IssueType.objects.get(pk=int(request.data["value"]))
            except IssueType.DoesNotExist:
                return Response({"error": "Issue Type not found."}, status=status.HTTP_404_NOT_FOUND)

            issue.issue_type = issue_type_obj

        else:
            setattr(issue, request.data["field"], request.data["value"])

        issue.save()
        return Response({"message": "Fields updated successfully."})