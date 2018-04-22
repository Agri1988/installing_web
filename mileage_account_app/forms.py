from django import forms
from .models import Car, MileageAccount, CarRefueling
from django.contrib.auth.models import User


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class MileageAccountWithInstallationForm(forms.ModelForm):
    class Meta:
        model = MileageAccount
        exclude = ['comments']

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(is_staff=False, is_active=True)


class MileageAccountWithOutInstallationForm(forms.ModelForm):
    class Meta:
        model = MileageAccount
        exclude = ['installation']

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(is_staff=False, is_active=True)


class CarRefuelingForm(forms.ModelForm):
    class Meta:
        model = CarRefueling
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['employee'].queryset = User.objects.filter(is_staff=False, is_active=True)


