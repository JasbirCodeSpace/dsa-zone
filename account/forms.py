from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from account.models import Student, Curator, User

class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password1", "password2")
    
    @transaction.atomic
    def save(self):
        user = super().save(commit = False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user = user)
        return user

class CuratorSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password1", "password2")
    
    @transaction.atomic
    def save(self):
        user = super().save(commit = False)
        user.is_curator = True
        user.save()
        staff = Curator.objects.create(user = user)
        return user

