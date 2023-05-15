from rest_framework import serializers
from user.models import *
class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","fullName","profile","email"]


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","fullName","email","profile"]

class ProfileAvtarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileAvtar
        fields = "__all__"