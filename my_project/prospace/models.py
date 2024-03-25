from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    # Add any other fields you need for both teachers and students

class Class(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='classes_taught')
    students = models.ManyToManyField(User, related_name='classes_enrolled', blank=True)
    # Add any other fields you need for the Class model

class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignments')
    classes = models.ManyToManyField(Class, related_name='assignments')
    # Add any other fields you need for the Assignment model

class Question(models.Model):
    question_text = models.TextField()
    # Add any other fields you need for the Question model
