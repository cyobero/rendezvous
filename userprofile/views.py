from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from schedule.models import Appointment
from django.contrib.auth.decorators import login_required
from login.models import UserProfile
from userprofile.forms import UserSearchForm

# Create your views here.
@login_required
def appointments_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    appointments = user_profile.appointments.all()
    return render(request, 'appointments/appointments.html', { 'appointments': appointments })


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(UserProfile, user=user)
    return render(request, 'profile.html', {'profile': profile})
