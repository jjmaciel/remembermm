from django import forms
from django.db.models import fields
from django import forms
from remembermm.models import PersonalData

class FormPersonalData(forms.ModelForm):
    class Meta:
        model = PersonalData
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }