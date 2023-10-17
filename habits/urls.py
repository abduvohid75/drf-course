from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter

from . import apps
from .views import index, HabitsViewSet, HabitsList

app_name = apps.HabitsConfig.name

router = DefaultRouter()
router.register('habits', HabitsViewSet, basename='habits-viewset')

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        description="API documentation for Habits model",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('', index, name='index'),
    path('', include(router.urls)),
    path('all-habits/', HabitsList.as_view(), name='all-habits'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
