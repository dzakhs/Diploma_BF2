from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}
class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=55, verbose_name='имя', **NULLABLE)
    surname = models.CharField(max_length=55, verbose_name='фамилия', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='Подтверждение почты')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
