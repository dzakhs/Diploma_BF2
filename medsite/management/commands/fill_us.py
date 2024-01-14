from django.core.management import BaseCommand

from medsite.models.UltraSound import USStudy


class Command(BaseCommand):
    def handle(self, *args, **options):
        us_list = [
            {
                'id': 1,
                'title': 'УЗИ',
                'area': 'почки',
                'description': 'обследование почек',
                'price': 1500,
                'doppler': False,
                'image': 'us/media/us_kidney.jpg'
            },
            {
                'id': 2,
                'title': 'УЗИ',
                'area': 'малый таз у женщин',
                'description': 'обследование органов малого таза у женщин',
                'price': 2500,
                'doppler': False,
                'image': 'us/media/us_taza.png'
            }

        ]
        study_for_create = []
        for study in us_list:
            study_for_create.append(USStudy(**study))

        USStudy.objects.all().delete()
        USStudy.objects.bulk_create(study_for_create)