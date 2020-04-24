from django.db import models
from django.contrib.auth.models import User
from login.models import UserProfile

# Create your models here.
class Appointment(models.Model):
    """Appointment is a SCHEDULED meeting between a `Booker` and an
    `Rendezvous`. It does not represent an actual `Meeting`."""
    booker = models.ManyToManyField(User, related_name='booker')
    rendezvous = models.ManyToManyField(User, related_name='rendezvous')
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return "Appointment {}: BKR: {} RDV: {}".format(self.id,
                                                        self.booker.username,
                                                        self.rendezvous.username)
