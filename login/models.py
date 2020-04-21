from django.db import models
from django.contrib.auth.models import User

# Create your models here.
PROFILE_TYPE_CHOICES = (
    ('B', 'BUYER'),
    ('D', 'DRIVER'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_type = models.CharField(max_length=1, choices=PROFILE_TYPE_CHOICES)
    image = models.ImageField(blank=True, null=True, upload_to='images/')

    def __str__(self):
        return self.user.username
