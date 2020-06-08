from django import forms
from django.db import models

class AcceptanceForm(forms.Form):
    Choices = (('A', 'Accept'), ('R', 'Reject'))
    choice = forms.ChoiceField(choices=Choices, widget=forms.RadioSelect)

class ItemReturnForm(forms.Form):
    Choices = (('Y', 'Returned'), ('N', 'Not-Returned'))
    choice = forms.ChoiceField(choices=Choices, widget=forms.RadioSelect)
