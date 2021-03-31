from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank = True, null = True)
    link = models.URLField(max_length=200, blank = True, null = True)
    difficulty = models.CharField(max_length=10)
    labels = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'questions'
        ordering =['-created_on']
