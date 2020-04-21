from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse

from registration.forms import RegisterForm

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('success'))
        else:
            messages.error(request, "Error")
        return render(request, 'registration/register.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})
