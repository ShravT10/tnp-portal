from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Custom user model
class User(AbstractUser):
    is_student = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
# Student profile data
class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    passing_year = models.IntegerField()
    skills = models.TextField(help_text="Comma-separated skills")
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)

    def __str__(self):
        return self.full_name