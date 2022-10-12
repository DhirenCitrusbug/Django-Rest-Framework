from dataclasses import fields
from rest_framework import serializers
from .models import MyModel, Student
from django.contrib.auth.models import User, Group

class Myserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyModel
        # fields = ['title','description']
        fields = '__all__'

# class StudentSerializer(serializers.Serializer):
#     rollno = serializers.CharField(max_length=100)
#     name = serializers.CharField(max_length=100)
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
      
class StudentSerializer(serializers.ModelSerializer):
    enroll = serializers.SerializerMethodField()

    class Meta:
        model=Student
        # fields = '__all__'
        fields = ['enroll','rollno','name']

    def get_enroll(self,obj):
        return obj.rollno+'-'+obj.name


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
