from django.db import models
from user.models import *
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    key = models.CharField(max_length=10)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="projects",on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "project"

class Team(models.Model):
    project = models.ForeignKey(Project,related_name="team",on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="members",on_delete=models.CASCADE)
    role = models.ForeignKey(Role,related_name="role",on_delete=models.CASCADE)

    class Meta:
        db_table = "team"