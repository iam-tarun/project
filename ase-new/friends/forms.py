from django import forms
from django.db import models

class FriendRequestForm(forms.Form):
    username = forms.CharField(max_length=20)

class AcceptForm(forms.Form):
    Choices = (('A', 'Accept'), ('R', 'Reject'))
    choice = forms.ChoiceField(choices=Choices, widget=forms.RadioSelect)
