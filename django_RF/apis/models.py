from django.db import models
from django.forms import CharField

# Create your models here.
class MyModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Student(models.Model):
    rollno = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name

