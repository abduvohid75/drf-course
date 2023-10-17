from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, CustomAuthToken, get_user_info

app_name = UsersConfig.name

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', CustomAuthToken.as_view(), name='login'),
    path('my-info', get_user_info, name="get_user_info"),
]
