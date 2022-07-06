from django.contrib import admin
from django.urls import include, path  # new
from rest_framework.schemas import get_schema_view # new

from rest_framework import permissions # new

from drf_yasg2.views import get_schema_view # new

from drf_yasg2 import openapi # new

schema_view = get_schema_view( # new
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="A sample API for learning DRF",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="hello@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),  # new
    path('api-auth/', include('rest_framework.urls')), # new
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')), # new
    path('api/v1/dj-rest-auth/registration/', # new
        include('dj_rest_auth.registration.urls')),
    # path('openapi', get_schema_view( # new
    #     title="Blog API",
    #     description="A sample API for learning DRF",
    #     version="1.0.0"
    # ), name='openapi-schema'),
    # new below...
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),

]
