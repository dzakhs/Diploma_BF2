from django.conf.urls.static import static
from django.urls import path

from config import settings
from medsite.apps import MedsiteConfig
from medsite.views import IndexListView, MRIStudyListView, CTStudyListView, USStudyListView, PETCTStudyListView, \
    MRIOrderCreateView, CTOrderCreateView, USOrderCreateView, PETCTOrderCreateView, USOrderDetailView, \
    PETCTOrderDetailView, CTOrderDetailView, MRIOrderDetailView, USOrderUpdateView, PETCTOrderUpdateView, \
    CTOrderUpdateView, MRIOrderUpdateView, USOrderDeleteView, PETCTOrderDeleteView, CTOrderDeleteView, \
    MRIOrderDeleteView

app_name = MedsiteConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('mri/', MRIStudyListView.as_view(), name='mri_list'),
    path('ct/', CTStudyListView.as_view(), name='ct_list'),
    path('us/', USStudyListView.as_view(), name='us_list'),
    path('petct/', PETCTStudyListView.as_view(), name='petct_list'),
    path('mri_order/', MRIOrderCreateView.as_view(), name='mri_order'),
    path('ct_order/', CTOrderCreateView.as_view(),name='ct_order'),
    path('us_order/', USOrderCreateView.as_view(),name='us_order'),
    path('petct_order/', PETCTOrderCreateView.as_view(),name='petct_order'),
    path('us_order/<int:pk>/', USOrderDetailView.as_view(),name='us_order_detail'),
    path('petct_order/<int:pk>/', PETCTOrderDetailView.as_view(),name='petct_order_detail'),
    path('ct_order/<int:pk>/', CTOrderDetailView.as_view(),name='ct_order_detail'),
    path('mri_order/<int:pk>/', MRIOrderDetailView.as_view(),name='mri_order_detail'),
    path('us_order/update/<int:pk>/', USOrderUpdateView.as_view(),name='us_order_update'),
    path('petct_order/update/<int:pk>/', PETCTOrderUpdateView.as_view(),name='petct_order_update'),
    path('ct_order/update/<int:pk>/', CTOrderUpdateView.as_view(),name='ct_order_update'),
    path('mri_order/update/<int:pk>/', MRIOrderUpdateView.as_view(),name='mri_order_update'),
    path('us_order/delete/<int:pk>/', USOrderDeleteView.as_view(),name='us_order_delete'),
    path('petct_order/delete/<int:pk>/', PETCTOrderDeleteView.as_view(),name='petct_order_delete'),
    path('ct_order/delete/<int:pk>/', CTOrderDeleteView.as_view(),name='ct_order_delete'),
    path('mri_order/delete/<int:pk>/', MRIOrderDeleteView.as_view(),name='mri_order_delete')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)