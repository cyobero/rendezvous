from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', ]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'input100',
                'placeholder': 'username',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'input100',
                'placeholder': 'password',
            })
        }
