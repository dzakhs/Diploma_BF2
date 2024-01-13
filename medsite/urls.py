from django.urls import path

from medsite.apps import MedsiteConfig
from medsite.views import IndexListView, MRIStudyListView, CTStudyListView, USStudyListView, PETCTStudyListView

app_name = MedsiteConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('mri/', MRIStudyListView.as_view(), name='mri_list'),
    path('ct/', CTStudyListView.as_view(), name='ct_list'),
    path('us/', USStudyListView.as_view(), name='us_list'),
    path('petct/', PETCTStudyListView.as_view(), name='petct_list'),
]