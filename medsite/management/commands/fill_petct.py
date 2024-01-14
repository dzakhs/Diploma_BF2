from django.core.management import BaseCommand

from medsite.models.PET_CT import PETCTStudy


class Command(BaseCommand):
    def handle(self, *args, **options):
        petct_list = [
            {
                'id': 1,
                'title': 'ПЭТ-КТ',
                'area': 'головной мозг',
                'description': 'оценка метаболической активности головного мозга',
                'price': 22000,
                'contrast_enhancement': False,
                'pet_tracer': '18F-FDG',
                'image': 'petct/media/petct_brain_fdg.jpg'
            },
            {
                'id': 2,
                'title': 'ПЭТ-КТ',
                'area': 'головной мозг',
                'description': 'оценка метаболической активности опухолевой ткани в головного мозге',
                'price': 32000,
                'contrast_enhancement': False,
                'pet_tracer': '11C-methionine',
                'image': 'petct/media/petct_meth.png'
            },
            {
                'id': 3,
                'title': 'ПЭТ-КТ',
                'area': 'все тело',
                'description': 'оценка метаболической активности опухолевой ткани',
                'price': 35000,
                'contrast_enhancement': True,
                'pet_tracer': '18F-FDG',
                'image': 'petct/media/petct_body.jpg'
            }

        ]
        study_for_create = []
        for study in petct_list:
            study_for_create.append(PETCTStudy(**study))

        PETCTStudy.objects.all().delete()
        PETCTStudy.objects.bulk_create(study_for_create)