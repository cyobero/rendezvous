from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from django.db.models import Q
from schedule.models import Appointment
from django.contrib.auth.models import User
from login.models import UserProfile


class ScheduleForm(forms.ModelForm):
    RENDEZVOUS_CHOICES = UserProfile.objects.all()
    rendezvous = forms.ModelChoiceField(queryset=RENDEZVOUS_CHOICES)
    class Meta:
        model = Appointment
        fields = ['rendezvous', 'date', 'time', ]
        widgets = {  
            'rendezvous': forms.Select(attrs={
                'class': 'input100 form-control',
            }),
            'date': forms.DateInput(attrs={
                'class': 'input100 form-control datepicker',
                'placeholder': 'Date',
                'type': 'date'
            }),
            'time': forms.TimeInput(attrs={
                'class': 'input100 form-control',
                'placeholder': 'Time',
                'type': 'time'
            })
        }
