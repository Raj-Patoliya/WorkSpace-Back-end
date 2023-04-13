import django.contrib.auth
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .usermanager import CustomUserManager
# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "role"

class User(AbstractBaseUser,PermissionsMixin):
    username = None
    fullName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='images/', blank=True, max_length=1000)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    object = CustomUserManager()

    def __str__(self):
        return f"{self.email}"

    class Meta:
        db_table = "user"