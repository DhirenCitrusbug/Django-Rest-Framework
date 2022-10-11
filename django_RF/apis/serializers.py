from dataclasses import fields
from rest_framework import serializers
from .models import MyModel, Student
from django.contrib.auth.models import User, Group

class Myserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyModel
        fields = ['title','description']

# class StudentSerializer(serializers.Serializer):
#     rollno = serializers.CharField(max_length=100)
#     name = serializers.CharField(max_length=100)
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
      
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        # fields = '__all__'
        fields = ['rollno','name']



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
      