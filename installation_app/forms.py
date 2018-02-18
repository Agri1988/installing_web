from django import forms
from .models import Installation, InstallationStandart,InstallationType, InstallationImage
from django.contrib.auth.models import User

class InstallationFormUser(forms.ModelForm):
    class Meta:
        model = Installation
        exclude = ['accepted']

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['employee_1'].queryset = User.objects.filter(is_staff=False, is_active=True)
        self.fields['employee_2'].queryset = User.objects.filter(is_staff=False, is_active=True)
        self.fields['employee_3'].queryset = User.objects.filter(is_staff=False, is_active=True)


class InstallationFormAdmin(forms.ModelForm):
    class Meta:
        model = Installation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['employee_1'].queryset = User.objects.filter(is_staff=False, is_active=True)
        self.fields['employee_2'].queryset = User.objects.filter(is_staff=False, is_active=True)
        self.fields['employee_3'].queryset = User.objects.filter(is_staff=False, is_active=True)


class InstallationStandartForm(forms.ModelForm):
    class Meta:
        model = InstallationStandart
        fields = '__all__'


class InstallationTypeForm(forms.ModelForm):
    class Meta:
        model = InstallationType
        fields = '__all__'


class InstallationImageForm(forms.ModelForm):
    class Meta:
        model = InstallationImage
        fields = ['image']