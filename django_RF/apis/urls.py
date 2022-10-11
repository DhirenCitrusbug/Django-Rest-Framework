from django.urls import include, path
# import routers
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'home', MyViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('students/', StudentGet.as_view()),
    path('student-detail/<int:pk>', student_detail),
]