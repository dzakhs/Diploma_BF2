# Generated by Django 4.2.2 on 2024-01-14 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petctorder',
            name='duration',
            field=models.DurationField(default=60.0, verbose_name='продолжительность'),
        ),
    ]
