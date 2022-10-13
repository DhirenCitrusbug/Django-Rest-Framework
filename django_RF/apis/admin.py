from django.contrib import admin
from .models import Brand, Product, Student,MyModel
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display =['id','rollno','name']

class BrandAdmin(admin.ModelAdmin):
    list_display =['id','name']

class ProductAdmin(admin.ModelAdmin):
    list_display =['id','product_name','brand','product_price']
admin.site.register(MyModel)
admin.site.register(Student,StudentAdmin)
admin.site.register(Brand,BrandAdmin)
admin.site.register(Product,ProductAdmin)

