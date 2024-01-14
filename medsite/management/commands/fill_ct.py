from django.core.management import BaseCommand

from medsite.models.CT import CTStudy



class Command(BaseCommand):
    def handle(self, *args, **options):
        ct_list = [
            {
                'id': 1,
                'title': 'КТ',
                'area': 'головной мозг',
                'description': 'ангиография сосудов головного мозга',
                'price': 7000,
                'contrast_enhancement': True,
                'image': 'ct/media/ct_brain.jpg'
            },
            {
                'id': 2,
                'title': 'КТ',
                'area': 'органы грудной полости',
                'description': 'структурное изображение органов грудной полости',
                'price': 3500,
                'contrast_enhancement': False,
                'image': 'ct/media/ct_lungs.jpg'
            },
            {
                'id': 3,
                'title': 'КТ',
                'area': 'органы брюшной полости',
                'description': 'структурное изображение органов брюшной полости с 3х фазным контрастированием',
                'price': 12000,
                'contrast_enhancement': True,
                'image': 'ct/media/ct_abdomen.jpg'
            },
            {
                'id': 4,
                'title': 'КТ',
                'area': 'тазобедренные суставы',
                'description': 'структурное изображение тазобедренных суставов',
                'price': 4000,
                'contrast_enhancement': False,
                'image': 'ct/media/ct_hips.jpg'
            }

        ]
        study_for_create = []
        for study in ct_list:
            study_for_create.append(CTStudy(**study))

        CTStudy.objects.all().delete()
        CTStudy.objects.bulk_create(study_for_create)