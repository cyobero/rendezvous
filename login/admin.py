from django.contrib import admin
from login.models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'image', 'appointments', ]

admin.site.register(UserProfile, UserProfileAdmin)
