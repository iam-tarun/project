from django import forms
from django.contrib.auth.models import User
from .models import Profiles, Backgroundimage


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ['image', 'phone']


class BackgroundImageForm(forms.ModelForm):
    class Meta:
        model = Backgroundimage
        fields = ['bg']
