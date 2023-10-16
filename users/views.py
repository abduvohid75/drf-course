
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User

from .serializers import UserSerializer


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    def get_object(self, queryset=None):
        return self.request.user

@login_required
def change_password(request):
    if request.method == 'POST':
        user = request.user
        generated_password = make_password('12')
        user.set_password(generated_password)
        user.save()
        return render(request, 'users/password_change_done.html')
    else:
        return render(request, 'users/generate_password.html')

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
