from django.db import models

NULLABLE = {'blank': True, 'null': True}


class CTStudy(models.Model):
    title = models.CharField(max_length=255, verbose_name='наименование')
    area = models.CharField(max_length=255, verbose_name='область обследования')
    description = models.CharField(max_length=255, verbose_name='описание', **NULLABLE)
    contrast_enhancement = models.BooleanField(default=False, verbose_name='контрастное усиление')

    def __str__(self):
        return f'{self.title} {self.area} {self.contrast_enhancement}'

    class Meta:
        verbose_name = 'КТ-исследеование'
        verbose_name_plural = 'КТ-исследования'