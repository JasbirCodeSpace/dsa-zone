from rest_framework import serializers
from question.models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id','title', 'description', 'link', 'difficulty', 'labels', 'created_on', 'updated_on']