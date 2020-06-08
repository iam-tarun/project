from django import forms
from django.db import models

class RatingForm(forms.Form):
    Choices = (('Poor', '1'), ('Average', '2'), ('Good', '3'), ('Very Good', '4'), ('Excellent', '5'))

    choice = forms.ChoiceField(choices=Choices, widget=forms.RadioSelect)
