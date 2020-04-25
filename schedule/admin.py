from django.contrib import admin
from schedule.models import Appointment

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    fields = ['rendezvous', 'date', 'time', ]

admin.site.register(Appointment, AppointmentAdmin)
