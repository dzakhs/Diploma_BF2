from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}

class USStudy(models.Model):
    title = models.CharField(max_length=255, verbose_name='наименование')
    area = models.CharField(max_length=255, verbose_name='область обследования')
    description = models.CharField(max_length=255, verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='us_images/', verbose_name='изображение', **NULLABLE)
    price = models.IntegerField(verbose_name='цена')
    doppler = models.BooleanField(default=False, verbose_name='допплерография')

    def __str__(self):
        return f'{self.title} {self.area} {self.contrast_enhancement}'

    class Meta:
        verbose_name = 'УЗ-исследеование'
        verbose_name_plural = 'УЗ-исследования'


class USOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пациент')
    study = models.ForeignKey(USStudy, on_delete=models.CASCADE, verbose_name='исследование')
    date = models.DateTimeField(verbose_name='дата и время')
    duration = models.DurationField(verbose_name='продолжительность')

    def __str__(self):
        return f'{self.user}, {self.study}, {self.date}, {self.duration}'

    class Meta:
        verbose_name = 'запись на исследование'
        verbose_name_plural = "записи на исследования"
