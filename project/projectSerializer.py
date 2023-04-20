from rest_framework import serializers
from user.models import User,Role
from project.models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
class ProjectTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
