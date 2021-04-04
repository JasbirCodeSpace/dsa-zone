from django.contrib import admin
from django.urls import path, include
from question import views

urlpatterns = [
    path('', views.QuestionCreateList.as_view()),
    path('<int:pk>', views.QuestionRetrieveUpdateDelete.as_view()),
]