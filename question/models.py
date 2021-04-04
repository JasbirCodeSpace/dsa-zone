from django.db import models

class Question(models.Model):
    EASY = 1
    MEDIUM = 2
    DIFFICULT = 3
    LEVEL = (
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (DIFFICULT, 'Difficult'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank = True, null = True)
    link = models.URLField(max_length=200, blank = True, null = True)
    difficulty = models.IntegerField(choices = LEVEL, default = EASY)
    labels = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'questions'
        ordering =['-created_on']
