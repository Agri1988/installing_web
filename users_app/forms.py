from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'is_active']


class MyUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password1', 'first_name', 'last_name', 'email', 'is_active']