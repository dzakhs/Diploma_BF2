from django.contrib import admin

from medsite.models.CT import CTStudy
from medsite.models.MRI import MRIStudy
from medsite.models.PET_CT import PETCTStudy
from medsite.models.UltraSound import USStudy


@admin.register(CTStudy)
class CTStudyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'price', 'area', 'contrast_enhancement',)
    list_filter = ('area', 'price',)
    search_fields = ('area',)


@admin.register(MRIStudy)
class MRIStudyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'price', 'area', 'contrast_enhancement',)
    list_filter = ('area', 'price',)
    search_fields = ('area',)


@admin.register(USStudy)
class USStudyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'price', 'area', 'doppler',)
    list_filter = ('area', 'price',)
    search_fields = ('area',)


@admin.register(PETCTStudy)
class MRIStudyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'price', 'area', 'contrast_enhancement', 'pet_tracer',)
    list_filter = ('area', 'price', 'pet_tracer',)
    search_fields = ('area', 'pet_tracer',)