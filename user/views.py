from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView,Response,status
from rest_framework import generics
from user.serializer import UserListSerializer,ProfileAvtarSerializer,UserProfileSerializer
from user.models import User,ProfileAvtar
from issue.issueSerializer import GroupViseIssueSerializer
class UserRegistration(APIView):
    def post(self, request):
        user = User()
        user.email = request.data["email"]
        user.profile = request.data["profile"]
        user.fullName = request.data["fullName"]
        try:
            user.set_password(request.data["password"])
            user.save()
            return Response({"success": "Account created successfully"})
        except Exception:
            return Response({"error": "Something Went Wrong"})


class UserProfile(generics.ListCreateAPIView):
    queryset = ProfileAvtar.objects.all()
    serializer_class = ProfileAvtarSerializer

class UsersList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserListSerializer
class CurrentUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = UserProfileSerializer(User.objects.get(email=request.user))
        return Response({"currentUser":user.data},status=status.HTTP_200_OK)
class UserIssueBasicDetails(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = User.objects.get(email=request.user)
        serializer = GroupViseIssueSerializer(user)
        return Response(serializer.data)

class ChangeInformation(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        user = User.objects.get(email=request.user)
        if user.check_password(request.data["currentPassword"]):
            user.set_password(request.data["newPassword"])
            user.save()
            return Response({"success":"Password Changed Successfully"})
        else:
            return Response({"error": "Invalid Password"})

    def patch(self,request):
        user = User.objects.get(email=request.user)
        user.profile = request.data["profile"]
        user.save()
        return Response({"success",user},status=status.HTTP_200_OK)