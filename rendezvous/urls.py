"""rendezvous URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rendezvous.views import index_view
from login.views import login_view, success_view, logout_view
from registration.views import register_view
from schedule.views import schedule_view, schedule_success_view
from userprofile.views import appointments_view

urlpatterns = [
    # Add Django site authentication urls (for login, logout, and password mgmt)
    path('account/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('login/success/', success_view, name='success'),
    path('register/', register_view, name='register'),
    path('register/success', success_view, name='success'),
    path('logout/', logout_view, name='logout'),
    path('schedule/', schedule_view, name='schedule'),
    path('schedule/success', schedule_success_view, name='success_schedule'),
    path('appointments/', appointments_view, name='appointments'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
