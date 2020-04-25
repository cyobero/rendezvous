from django.db import models


# Create your models here.
class Appointment(models.Model):
    """Appointment is a SCHEDULED meeting between a `Booker` and an
    `Rendezvous`. It does not represent an actual `Meeting`."""
    rendezvous = models.ForeignKey('login.UserProfile', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    details = models.CharField(max_length=150, blank=True, null=True, default="No details provided.")
