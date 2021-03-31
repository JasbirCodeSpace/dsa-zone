from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin

from question.models import Question
from question.serializer import QuestionSerializer

class QuestionCreateList(GenericAPIView, CreateModelMixin, ListModelMixin):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class QuestionRetrieveUpdateDelete(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)