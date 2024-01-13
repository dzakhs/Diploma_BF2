from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class PETCTStudy(models.Model):

    PET_TRACER_CHOISES = (
        ('18F-FDG', '18F-фтордезоксиглюкоза'),
        ('11C-methionine', '11C-метионин'),
    )

    title = models.CharField(max_length=255, verbose_name='наименование')
    area = models.CharField(max_length=255, verbose_name='область обследования')
    description = models.CharField(max_length=255, verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='ct_images/', verbose_name='изображение', **NULLABLE)
    price = models.IntegerField(verbose_name='цена')
    contrast_enhancement = models.BooleanField(default=False, verbose_name='контрастное усиление')
    pet_tracer = models.CharField(max_length=55, choices=PET_TRACER_CHOISES, verbose_name='радиофармпрепарат')

    def __str__(self):
        return f'{self.title}, {self.area}, {self.contrast_enhancement}, {self.pet_tracer}'

    class Meta:
        verbose_name = 'ПЭТ/КТ-исследование'
        verbose_name_plural = 'ПЭТ/КТ-исследования'


class PETCTOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пациент')
    study = models.ForeignKey(PETCTStudy, on_delete=models.CASCADE, verbose_name='исследование')
    date = models.DateTimeField(verbose_name='дата и время')
    duration = models.DurationField(verbose_name='продолжительность')

    def __str__(self):
        return f'{self.user}, {self.study}, {self.date}, {self.duration}'

    class Meta:
        verbose_name = 'запись на исследование'
        verbose_name_plural = "записи на исследования"
