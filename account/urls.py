from django.contrib import admin
from django.urls import path, include
from account import views

urlpatterns = [

    path('signup/student', views.StudentCreateView.as_view(), name="student_signup"),
    path('signup/curator', views.CuratorCreateView.as_view(), name="curator_signup"),
]