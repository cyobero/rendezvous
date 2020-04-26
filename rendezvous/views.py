from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from userprofile.forms import UserSearchForm
from django.contrib.auth.models import User


def index_view(request):
    form = UserSearchForm(request.GET or None)
    if request.method == 'GET' and 'username' in request.GET:
        if form.is_valid():
            username = request.GET.get('username')
            users = User.objects.filter(username__icontains=username)
            return render(request, 'index.html', {'form': form, 'users': users})
        else:
            messages.error(request, 'Error')
    else:
        form = UserSearchForm()
        return render(request, 'index.html', {'form': form})
