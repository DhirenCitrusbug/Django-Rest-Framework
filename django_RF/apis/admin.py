from django.contrib import admin
from .models import Student,MyModel
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display =['id','rollno','name']
admin.site.register(MyModel)
admin.site.register(Student,StudentAdmin)