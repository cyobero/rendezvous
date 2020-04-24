from django.contrib import admin
from schedule.models import Appointment

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    fields = ['booker', 'rendezvous', 'date', 'time', ]

admin.site.register(Appointment, AppointmentAdmin)
