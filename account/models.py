from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_student = models.BooleanField(default = False)
    is_curator = models.BooleanField(default = False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)

class Curator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)