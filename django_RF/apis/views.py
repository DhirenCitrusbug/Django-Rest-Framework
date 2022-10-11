
from functools import partial
from webbrowser import get
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets,status
# Create your views here.
from .serializers import Myserializer, StudentSerializer
from .models import MyModel, Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from .serializers import UserSerializer, GroupSerializer
# create a viewset
class MyViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = MyModel.objects.all()
     
    # specify serializer to be used
    serializer_class = Myserializer

class StudentGet(APIView):
    def get(self,request):
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data)


@api_view(['GET','POST','DELETE',"PUT","PATCH"])
def student_detail(request,pk):
    if request.method == "GET":
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        except Exception as DoesNotExits:
            return Response({'msg':'Data Not Found'},status=status.HTTP_404_NOT_FOUND)

    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        try:
            pk = request.data.get('id')
            print(pk)
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Updated'})
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as DoesNotExits:
            return Response({'msg':'Data Not Found'},status=status.HTTP_404_NOT_FOUND)       

    elif request.method == "PATCH":
        try:
            pk = request.data['id']
            print(pk)
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Updated'})
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as DoesNotExits:
            return Response({'msg':'Data Not Found'},status=status.HTTP_404_NOT_FOUND)     
    elif request.method == "DELETE":
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response({'msg':'Data Deleted'})



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
