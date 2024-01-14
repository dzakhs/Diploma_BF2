from django.core.management import BaseCommand

from medsite.models.MRI import MRIStudy


class Command(BaseCommand):
    def handle(self, *args, **options):
        mri_list = [
            {
                'id': 1,
                'title': 'МРТ',
                'area': 'головной мозг',
                'description': 'структурное изображение головного мозга с контрастным усилением',
                'price': 9000,
                'contrast_enhancement': True,
                'image': 'mri/media/mrt_brain.jpg'
            },
            {
                'id': 2,
                'title': 'МРТ',
                'area': 'шейный отдел спинного мозга',
                'description': 'структурное изображение шейного отдела спинного мозга',
                'price': 5000,
                'contrast_enhancement': False,
                'image': 'mri/media/mrt_spinal.jpeg'
            },
            {
                'id': 3,
                'title': 'МРТ',
                'area': 'органы брюшной полости',
                'description': 'структурное изображение органов брюшной полости с контрастированием',
                'price': 12000,
                'contrast_enhancement': True,
                'image': 'mri/media/mrt_abdomen.jpg'
            },
            {
                'id': 4,
                'title': 'МРТ',
                'area': 'коленный сустав',
                'description': 'структурное изображение коленного сустава',
                'price': 4500,
                'contrast_enhancement': False,
                'image': 'mri/media/mrt_knee.jpg'
            }

        ]
        study_for_create = []
        for study in mri_list:
            study_for_create.append(MRIStudy(**study))

        MRIStudy.objects.all().delete()
        MRIStudy.objects.bulk_create(study_for_create)