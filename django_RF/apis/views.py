from rest_framework import viewsets,status
# Create your views here.
from .serializers import BrandSerializer,  Myserializer, ProductSerializer, StudentSerializer
from .models import Brand, MyModel, Product, Student
from .paginations import PaginationClass
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView
from .serializers import UserSerializer, GroupSerializer
from django.contrib.auth import login,logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.filters import SearchFilter,OrderingFilter


# create a viewset
class MyViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = MyModel.objects.all()
     
    # specify serializer to be used
    serializer_class = Myserializer

class StudentGet(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)        


@api_view(['GET','DELETE',"PUT","PATCH"])
def student_detail(request,pk):
    if request.method == "GET":
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        except Exception as DoesNotExits:
            return Response({'msg':'Data Not Found'},status=status.HTTP_404_NOT_FOUND)


    elif request.method == "PUT":
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Updated'})
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'msg':'Data Not Found'+str(e)},status=status.HTTP_404_NOT_FOUND)       

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

# class Login(APIView):
#     def post(self,request):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         user = authenticate(username=username, password=password)
#         if not user:
#             return Response({'error': 'Invalid Credentials'},
#                               status=status.HTTP_400_BAD_REQUEST)
#         user_serializer = UserSerializer(user,context={'request': request})
#         token, created = Token.objects.get_or_create(user=user)
#         return Response( {
#             'url':user_serializer.data['url'],
#             "username": user.username,
#             "token": token.key,
#         },status=status.HTTP_200_OK)
    




class ProductAPI(ListAPIView,APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields=['product_name','description',]
    ordering_fields =['product_price']
    pagination_class = PaginationClass


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



    # def get(self,request):
    #     search = request.query_params.get('search')
    #     products = Product.objects.all()
    #     # if search is not None:
    #     #     products = Product.objects.filter(product_name__contains=search)
    #     # else:
    #     #     products = Product.objects.all()
    #     serializer = ProductSerializer(products,many=True)
    #     return Response(serializer.data)


    def post(self,request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            # serializer.validated_data['brand_name']=request.data['brand_name']
            serializer.save()
            return Response({'msg':'Data Created','Data':serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)      

    def put(self,request,pk):


        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product,data=request.data,request=request)
            serializer._declared_fields['brand_name'].read_only=True
            if serializer.is_valid():
                serializer.save()
                
                return Response({'msg':'Data Updated','Data':serializer.data},status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        except Exception as e:
            return Response({'msg':'Data Not Found: '+str(e)},status=status.HTTP_404_NOT_FOUND)


    def patch(self,request,pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Updated','data':serializer.data},status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        except:
            return Response({'msg':'Data Not Found'},status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk):

        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response({'msg':'Data Deleted Successfully'},status=status.HTTP_200_OK)
        except:
            return Response({'msg':'Data Not Found'},status=status.HTTP_404_NOT_FOUND)


class ProductListAPI(ListAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()

    serializer_class = ProductSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields=['product_name']
    ordering_fields =['product_price','product_name']
    pagination_class = PaginationClass

class ProductDetailAPI(RetrieveAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_fields = ['id']

class BrandAPI(ListCreateAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_fields = ['id']
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields=['name']
    ordering_fields =['name']
    pagination_class = PaginationClass

class BrandDetailAPI(RetrieveUpdateDestroyAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_fields = ['id']
