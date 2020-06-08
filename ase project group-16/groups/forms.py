from django import forms
from django.db import models
from .models import GroupTable


class GroupCreationForm(forms.ModelForm):
    class Meta:
        model = GroupTable
        fields = ['name', 'desc', 'image']


class MemberAdditionForm(forms.Form):
    username = forms.CharField(max_length=20)


class InvitationForm(forms.Form):
    Choices = (('A', 'Accept'), ('R', 'Reject'))
    choice = forms.ChoiceField(choices=Choices, widget=forms.RadioSelect)


class LeaveGroupForm(forms.Form):
    Choices = (('Y', 'Yes'), ('N', 'No'))
    choice = forms.ChoiceField(choices=Choices, widget=forms.RadioSelect)
