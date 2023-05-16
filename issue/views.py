from django.shortcuts import render
# import boto3
# from botocore.exceptions import ClientError
from django.core.mail import send_mail,EmailMessage
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from project.projectSerializer import *
from issue.issueSerializer import *
from issue.models import *
from rest_framework.views import Response
from django.utils import timezone
import datetime

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
    # permission_classes = [IsAuthenticated]
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
class ActivityLogCRUDVIEW(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer

def send_email(subject,message):
    subject = subject
    body = f"<p style='font-size:20px;'>{message}</p>"
    from_email = "rajpatoliya888@gmail.com"
    to_email = ["rpatoliya888@gmail.com"]

    email = EmailMessage(subject, body, from_email, to_email)
    email.content_subtype = "html"  # Set the content type as HTML

    try:
        email.send()
        return True
    except Exception as e:
        print(f"An error occurred while sending the email: {str(e)}")
        return False

class IssueCRUDVIEW(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = IssueSerializer

    def post(self,request):
        project = Project.objects.filter(key=request.data["project"]).values("id").first()
        lastIndex = Issue.objects.filter(project_id=project["id"],status=int(request.data["status"])).order_by('-index').values("index").first()

        data = {
            "project": project["id"],
            "issue_type": int(request.data["issueType"]),
            "issue_description": request.data["description"],
            "status": int(request.data["status"]),
            "priority": int(request.data["priority"]),
            "issue_summary": request.data["summary"],
            "assignee": int(request.data["assignee"]),
            "reporter": int(request.data["reporter"]),
            "index":lastIndex["index"]+1,
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
                    return Response({"error": "Something went wrong"}, status=status.HTTP_404_NOT_FOUND)
            return Response({"created": "issue Created successfully."}, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response({"error": "Something went wrong"}, status=status.HTTP_404_NOT_FOUND)

class UpdateIssueFields(APIView):
    permission_classes = [IsAuthenticated]

    def get_user_name(self,email):
        user = User.objects.filter(email=email).values("fullName").first()
        return user['fullName']

    def get(self,request,issue_id):
        try:
            issue = Issue.objects.get(pk=issue_id)
            serializer = IssueSerializer(issue)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Issue.DoesNotExist:
            return Response({"error": serializer.errors}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, issue_id):
        message = ""
        subject = ""
        try:
            issue = Issue.objects.get(pk=issue_id)
            subject = f"Issue of {issue.project.key} has Been Updated"
        except Issue.DoesNotExist:
            return Response({"error": "Issue not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.data["field"] == 'status':
            try:
                status_obj = Status.objects.get(pk=int(request.data["value"]))
                message = f"{self.get_user_name(request.user)} has changed Status of issue {issue.project.key}-" \
                          f"{issue.id} to " \
                          f"{issue.status} to {status_obj}"
            except Status.DoesNotExist:
                return Response({"error": "Status not found."}, status=status.HTTP_404_NOT_FOUND)
            issue.status = status_obj
        elif request.data["field"] == 'priority':
            try:
                priority_obj = Priority.objects.get(pk=int(request.data["value"]))
            except Priority.DoesNotExist:
                return Response({"error": "Priority not found."}, status=status.HTTP_404_NOT_FOUND)
            message = f"{self.get_user_name(request.user)} has changed Priority of issue {issue.project.key}-" \
                      f"{issue.id} to " \
                      f"{issue.priority} to {priority_obj}"
            issue.priority = priority_obj

        elif request.data["field"] == 'assignee':
            try:
                assignee_obj = User.objects.get(pk=int(request.data["value"]))
            except User.DoesNotExist:
                return Response({"error": "Assignee not found."}, status=status.HTTP_404_NOT_FOUND)
            message = f"{self.get_user_name(request.user)} has changed Assignee of issue {issue.project.key}-" \
                      f"{issue.id}, From " \
                      f"{self.get_user_name(issue.assignee)} to {self.get_user_name(assignee_obj)}"
            issue.assignee = assignee_obj

        elif request.data["field"] == 'reporter':
            try:
                reporter_obj = User.objects.get(pk=int(request.data["value"]))
            except User.DoesNotExist:
                return Response({"error": "Reporter not found."}, status=status.HTTP_404_NOT_FOUND)
            message = f"{self.get_user_name(request.user)} has changed Assignee of issue {issue.project.key}-" \
                      f"{issue.id}, From " \
                      f"{self.get_user_name(issue.reporter)} to {self.get_user_name(reporter_obj)}"
            issue.reporter = reporter_obj

        elif request.data["field"] == 'issue_type_id':
            try:
                issue_type_obj = IssueType.objects.get(pk=int(request.data["value"]))
            except IssueType.DoesNotExist:
                return Response({"error": "Issue Type not found."}, status=status.HTTP_404_NOT_FOUND)
            message = f"{self.get_user_name(request.user)} has changed Assignee of issue {issue.project.key}-" \
                      f"{issue.id}, From " \
                      f"{issue.issue_type} to {issue_type_obj}"
            issue.issue_type = issue_type_obj

        else:
            setattr(issue, request.data["field"], request.data["value"])
            message = f"{self.get_user_name(request.user)} has changed Assignee of issue {issue.project.key}-" \
                      f"{issue.id}, From " \
                      f"\"{issue.issue_summary}\" to {request.data['value']}"
        issue.updated_date = datetime.datetime.now(tz=timezone.utc)
        issue.save()

        teamArr = list()
        team = TeamEmailAddress(Team.objects.filter(project_id=issue.project.id),many=True)
        to_email = list()
        for team in team.data:
            teamArr.append(team["email"])
        for team in teamArr:
            to_email.append(team["email"])
        send_email(subject,message,to_email)
        return Response({"message": "Fields updated successfully."},status=status.HTTP_200_OK)

class PostCommentIssue(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,issue_id):
        print(issue_id)
        comment = Comment.objects.filter(issue_id=issue_id)
        serializer = CommentSerializer(comment,many=True)
        return Response({'success': serializer.data}, status=status.HTTP_200_OK)

    def post(self,request):
        data = {
            "comment_text":request.data['comment_text'],
            "user_id":int(request.data['user_id']),
            "issue_id":int(request.data['issue_id']),
        }
        print(data)
        serializer = CreateCommentatorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            comment = Comment.objects.filter(issue_id=int(request.data['issue_id']),user_id=int(request.data['user_id'])).last()
            lastcomment = CommentSerializer(comment)
            return Response({'lastcomment':lastcomment.data},status=status.HTTP_200_OK)
        else:
            return Response({'Error':serializer.errors},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self,request,pk):
        comment = Comment.objects.filter(pk=pk).delete()
        return Response({"success":"Comment deleted successfully"})

    def patch(self,request,pk):
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Response({"error": "Comment not found."}, status=status.HTTP_404_NOT_FOUND)
        comment.comment_text = request.data["comment_text"]
        comment.save()
        return Response({"success": "Comment Updated successfully"})