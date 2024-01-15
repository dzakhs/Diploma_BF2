from django.contrib import admin

from medsite.models.CT import CTStudy, CTOrder
from medsite.models.MRI import MRIStudy, MRIOrder
from medsite.models.PET_CT import PETCTStudy, PETCTOrder
from medsite.models.UltraSound import USStudy, USOrder


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


@admin.register(CTOrder)
class CTOrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'study', 'date', 'duration', )
    list_filter = ('user', 'study',)
    search_fields = ('date',)

@admin.register(PETCTOrder)
class PETCTOrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'study', 'date', 'duration', )
    list_filter = ('user', 'study',)
    search_fields = ('date',)


@admin.register(MRIOrder)
class MRIOrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'study', 'date', 'duration', )
    list_filter = ('user', 'study',)
    search_fields = ('date',)


@admin.register(USOrder)
class USOrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'study', 'date', 'duration',)
    list_filter = ('user', 'study',)
    search_fields = ('date',)