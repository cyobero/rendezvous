from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, reverse, redirect
from login.forms import LoginForm

# Create your views here.
def login_view(request):
    errors = []
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect(reverse('index'))
        else:
            errors.append("Invalid credentials. Please try again.")
            return render(request, 'registration/login.html', {'form': form,
                                                               'errors': errors})
    else:
        return render(request, 'registration/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('login'))


@login_required
def success_view(request):
    return redirect(reverse('index'))
