from django.db import models
from user.models import *
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    key = models.CharField(max_length=10)
    description = models.TextField()
    stat_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

class Team(models.Model):
    project = models.ForeignKey(Project,related_name="project",on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="members",on_delete=models.CASCADE)