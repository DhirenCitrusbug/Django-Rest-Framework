from rest_framework import serializers

from .models import Brand, MyModel, Product, Student
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



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class LoginSerializer(serializers.Serializer):
      username = serializers.CharField(max_length=100)
      password = serializers.CharField(max_length=100)    

    

class BrandSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True)
    class Meta:
        model = Brand
        fields = ['name','products']

class ReadWriteSerializerMethodField(serializers.SerializerMethodField):
    def __init__(self, method_name=None, **kwargs):
        self.method_name = method_name
        kwargs['source'] = '*'
        kwargs['read_only'] = False
        super(serializers.SerializerMethodField, self).__init__(**kwargs)

    def to_internal_value(self, data):
        return {self.field_name: data}

class ProductSerializer(serializers.ModelSerializer):
    brand_name = ReadWriteSerializerMethodField()
    class Meta:
        model = Product
        fields = ['product_name','product_price','description','brand','brand_name']
        read_only_fields = ('brand',)
        
    def __init__(self, instance=None, data=...,request=None, **kwargs):
        print(data,'dfdf',...)
        try:
            if request.method == 'PUT' or request.method == 'PATCH':
                self._declared_fields['brand_name']=serializers.SerializerMethodField()
                print(self._declared_fields['brand_name'].read_only,'here')
        except:
            pass
        super().__init__(instance, data, **kwargs)

    def get_brand_name(self,obj):
 
        return Brand.objects.get(id=obj.brand.id).name


    def create(self,validated_data):
        product_name = validated_data['product_name']
        brand,created = Brand.objects.get_or_create(name=validated_data['brand_name'])
        product_price = validated_data['product_price']
        description = validated_data['description']
        return Product.objects.create(product_name=product_name,brand=brand,product_price=product_price,description=description)

    def update(self, instance, validated_data):
        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.product_price = validated_data.get('product_price', instance.product_price)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


