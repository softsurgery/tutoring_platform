from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, permissions  
from drf_yasg.views import get_schema_view  
from drf_yasg import openapi  

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


schema_view = get_schema_view(  
    openapi.Info(  
        title="Tutoring Platform",  
        default_version='v1',  
        description="Tutoring Platform under development",  
        terms_of_service="",  
        contact=openapi.Contact(email="contact@example.com"),  
        license=openapi.License(name="Awesome License"),  
    ),  
    public=True,  
    permission_classes=(permissions.AllowAny,),  
)  

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('basic.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  
]