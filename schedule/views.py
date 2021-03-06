from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from schedule.forms import ScheduleForm
from schedule.models import Appointment
from django.contrib.auth.models import User
from login.models import UserProfile

# Create your views here.
@login_required
def schedule_view(request):
    booker = UserProfile.objects.get(user=request.user)
    form = ScheduleForm(request.POST or None)
    if form.is_valid():
        form = form.clean()
        rendezvous = form['rendezvous']
        date = form['date']
        time = form['time']
        details = form['details']
        # Create and save new `Appointment` object.
        appt = Appointment.objects.create(rendezvous=rendezvous, date=date, time=time, details=details)
        booker.appointments.add(appt)
        return redirect(reverse('success_schedule'))
    else:
        messages.error(request, "error")
    return render(request, 'schedule/schedule_form.html', {'form':form})


@login_required
def schedule_success_view(request):
    return render(request, 'schedule/success.html')
