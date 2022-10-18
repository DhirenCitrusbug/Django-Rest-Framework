from django.urls import include, path,re_path
# import routers
from rest_framework import routers
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


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
    # path('login/',Login.as_view()),
    path('products/',ProductAPI.as_view()),
    path('products/<int:pk>',ProductAPI.as_view()),
    path('brands/',BrandAPI.as_view()),
    path('products-list/',ProductListAPI.as_view()),
    path('brand/<int:pk>',BrandDetailAPI.as_view()),
    path('product-detail/<int:pk>',ProductDetailAPI.as_view()),
    re_path(r'^api/api.json$', schema_view.without_ui(cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),


]