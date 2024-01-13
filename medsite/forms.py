from django.forms import forms

from medsite.models.CT import CTOrder
from medsite.models.MRI import MRIOrder
from medsite.models.PET_CT import PETCTOrder
from medsite.models.UltraSound import USOrder


class MRIOrderForm(forms.ModelForm):
    class Meta:
        model = MRIOrder
        fields = '__all__'


class CTOrderForm(forms.ModelForm):
    class Meta:
        model = CTOrder
        fields = '__all__'


class USOrderForm(forms.ModelForm):
    class Meta:
        model = USOrder
        fields = '__all__'


class PETCTOrderForm(forms.ModelForm):
    class Meta:
        model = PETCTOrder
        fields = '__all__'
