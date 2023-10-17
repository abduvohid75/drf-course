from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser, models.Model):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')

    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='аватар', null=True, blank=True)
    phone = models.CharField(max_length=35, verbose_name='телефон', null=True, blank=True)
    country = models.CharField(max_length=30, verbose_name='страна', null=True, blank=True)

    is_email_verified = models.BooleanField(default=False, verbose_name='статус верификации email')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
