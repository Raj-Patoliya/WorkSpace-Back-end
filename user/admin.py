from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id","fullName",
                  "email","password","profile",
                  "is_active","is_staff",
                  "is_superuser","is_verified"]
@admin.register(Role)
class UserRole(admin.ModelAdmin):
    list_display = [
        'id','name','description',
    ]