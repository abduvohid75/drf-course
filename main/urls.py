from django.contrib import admin
from django.urls import path, include
from habits.views import HabitsViewSet, get_user_info
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('habits', HabitsViewSet, basename='habits-viewset')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('habits.urls', namespace='habits')),
    path('', include('users.urls', namespace='users')),
    path('api/', include(router.urls)),
    path('api/my-info/', get_user_info, name="getuserinfo"),
]
