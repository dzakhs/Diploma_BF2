from django import forms
from django.forms import SplitHiddenDateTimeWidget

from medsite.models.CT import CTOrder
from medsite.models.MRI import MRIOrder
from medsite.models.PET_CT import PETCTOrder
from medsite.models.UltraSound import USOrder


class MRIOrderForm(forms.ModelForm):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    class Meta:
        model = MRIOrder
        fields = ('user', 'study', 'date')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CTOrderForm(forms.ModelForm):
    class Meta:
        model = CTOrder
        fields = ('user', 'study', 'date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class USOrderForm(forms.ModelForm):
    class Meta:
        model = USOrder
        fields = ('user', 'study', 'date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class PETCTOrderForm(forms.ModelForm):
    class Meta:
        model = PETCTOrder
        fields = ('user', 'study', 'date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
