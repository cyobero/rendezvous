from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Rendezvous(models.Model):
    """Rendezvous is the object's appointment (e.g. repairman, barber, etc.)"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username


class Appointment(models.Model):
    """Appointment is a SCHEDULED meeting between a `Booker` and an
    `Rendezvous`. It does not represent an actual `Meeting`."""
    booker = models.OneToOneField(User, on_delete=models.CASCADE)
    rendezvous = models.OneToOneField(Rendezvous, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return "Appointment {}: BKR: {} RDV: {}".format(self.id,
                                                        self.booker.username,
                                                        self.rendezvous.user.username)
