from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from schedule.models import Appointment
from django.contrib.auth.models import User


class ScheduleForm(forms.ModelForm):
    RENDEZVOUS_CHOICES = User.objects.all()
    rendezvous = forms.ModelChoiceField(queryset=RENDEZVOUS_CHOICES)
    class Meta:
        model = Appointment
        fields = ['rendezvous', 'date', 'time', ]
        widgets = {
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
