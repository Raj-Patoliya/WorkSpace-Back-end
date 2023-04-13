from rest_framework import serializers
from user.models import *
class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"