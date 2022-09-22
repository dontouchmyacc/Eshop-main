
from django.urls import path

from drf_yasg.views import get_schema_view as swagger_get_schema_view
from drf_yasg import openapi




schema_view = swagger_get_schema_view(
   openapi.Info(
      title ='store API',
      default_version='1.0.0',
      description='API documentation of App',
   ),
   public=True,
)
   
urlpatterns = [
   path('swagger/schema/',schema_view.with_ui('swagger',cache_timeout=0), name='swagger-schema'),
]