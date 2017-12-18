from django import forms
from .models import Installation

class InstallationFormUser(forms.ModelForm):
    class Meta:
        model = Installation
        exclude = ['accepted']

class InstallationFormAdmin(forms.ModelForm):
    class Meta:
        model = Installation
        fields = '__all__'