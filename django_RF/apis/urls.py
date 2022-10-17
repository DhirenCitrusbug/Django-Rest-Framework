from django.urls import include, path
# import routers
from rest_framework import routers
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView
router = routers.DefaultRouter()
router.register(r'mymodel', MyViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('students/', StudentGet.as_view()),
    path('student/<int:pk>', student_detail),
    path('gettoken/',obtain_auth_token),
    path('login/',Login.as_view()),
    path('products/',ProductAPI.as_view()),
    path('products/<int:pk>',ProductAPI.as_view()),
    path('brands/',BrandAPI.as_view()),
    path('products-list/',ProductListAPI.as_view()),
    path('brand/<int:pk>',BrandDetailAPI.as_view()),
    path('product-detail/<int:pk>',ProductDetailAPI.as_view()),

]