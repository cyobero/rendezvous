from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'input100',
        'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input100',
        'placeholder': 'Confirm password'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'input100',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input100',
                'placeholder': 'Email',
                'required': 'true'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'input100',
                'placeholder': 'Password',
            })
        }
