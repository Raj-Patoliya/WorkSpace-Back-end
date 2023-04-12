from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Project)
class Project(admin.ModelAdmin):
    list_display = ["id","title",'description',"stat_date"]
@admin.register(Team)
class ProjectTeam(admin.ModelAdmin):
    list_display = [
        'id','project_id','user_id'
    ]