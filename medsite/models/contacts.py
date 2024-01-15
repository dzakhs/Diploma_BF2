from django.db import models

from users.models import NULLABLE


class Contacts(models.Model):
    name = models.CharField(max_length=255, verbose_name='имя')
    email = models.CharField(max_length=150, verbose_name='e-mail')
    phone = models.CharField(max_length=10, verbose_name='телефон')
    message = models.TextField(**NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta():
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'