from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, reverse

from registration.forms import RegisterForm

# Create your views here.
def register_view(request):
    errors = []
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()  # load profile instance created by signal
        user.user_profile.birthdate = form.cleaned_data.get('birthdate')
        user.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect(reverse('success'))
    else:
        return render(request, 'registration/register.html', {'form': form})
