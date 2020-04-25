from django.shortcuts import render
from schedule.models import Appointment
from django.contrib.auth.decorators import login_required
from login.models import UserProfile

# Create your views here.
@login_required
def appointments_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    appointments = user_profile.appointments.all()
    return render(request, 'appointments/appointments.html', { 'appointments': appointments })
