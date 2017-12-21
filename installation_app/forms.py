from django import forms
from .models import Installation
from django.contrib.auth.models import User

class InstallationFormUser(forms.ModelForm):
    class Meta:
        model = Installation
        exclude = ['accepted']

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['employee_1'].queryset = User.objects.filter(is_staff=False)
        self.fields['employee_2'].queryset = User.objects.filter(is_staff=False)
        self.fields['employee_3'].queryset = User.objects.filter(is_staff=False)


class InstallationFormAdmin(forms.ModelForm):
    class Meta:
        model = Installation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['employee_1'].queryset = User.objects.filter(is_staff=False)
        self.fields['employee_2'].queryset = User.objects.filter(is_staff=False)
        self.fields['employee_3'].queryset = User.objects.filter(is_staff=False)