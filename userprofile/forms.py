from django import forms
from django.contrib.auth.models import User


class UserSearchForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Search users',
    }))
