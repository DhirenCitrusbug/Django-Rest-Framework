from email.policy import default
from enum import unique
from pyexpat import model
from unicodedata import name
from django.db import models
from django.forms import CharField
from autoslug import AutoSlugField
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

class Brand(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='products')
    product_price = models.PositiveIntegerField()
    description = models.TextField()
    def __str__(self):
        return self.product_name
