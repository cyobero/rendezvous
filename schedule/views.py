from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from schedule.forms import ScheduleForm
from schedule.models import Appointment, Rendezvous

# Create your views here.
@login_required
def schedule_view(request):
    booker = request.user
    form = ScheduleForm(request.POST or None)
    if form.is_valid():
        rendezvous_list = Rendezvous.objects.all()
        form = form.clean()
        form = form.cleaned_data.get('rendezvous')
        date = form.cleaned_data.get('date')
        time = form.cleaned_data.get('time')
        # Create and save new `Appointment` object.
        appt = Appointment(booker=booker, rendezvous=rendezvous, date=date,
                           time=time).save()
        return redirect(reverse('success_schedule'))
    else:
        messages.error(request, "error")
    return render(request, 'schedule/schedule_form.html', {'form':form})
