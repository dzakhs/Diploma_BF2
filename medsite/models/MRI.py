from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class MRIStudy(models.Model):
    title = models.CharField(max_length=255, verbose_name='наименование')
    area = models.CharField(max_length=255, verbose_name='область обследования')
    description = models.CharField(max_length=255, verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='mri_images/', verbose_name='изображение', **NULLABLE)
    price = models.IntegerField(verbose_name='цена')
    contrast_enhancement = models.BooleanField(default=False, verbose_name='контрастное усиление')

    def __str__(self):
        return f'{self.title} {self.area} '

    class Meta:
        verbose_name = 'МРТ-исследование'
        verbose_name_plural = 'МРТ-исследования'


class MRIOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пациент')
    study = models.ForeignKey(MRIStudy, on_delete=models.CASCADE, verbose_name='исследование')
    date = models.DateTimeField(verbose_name='дата и время')
    duration = models.DurationField(default=60.00, verbose_name='продолжительность')

    def __str__(self):
        return f'{self.user}, {self.study}, {self.date}, {self.duration}'


    class Meta:
        verbose_name = 'запись на исследование МРТ'
        verbose_name_plural = "записи на исследования МРТ"
