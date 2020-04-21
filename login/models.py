from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
PROFILE_TYPE_CHOICES = (
    ('B', 'BOOKER'),
    ('A', 'APPOINTEE'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_type = models.CharField(max_length=1, choices=PROFILE_TYPE_CHOICES)
    birthdate = models.DateField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='images/')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = UserProfile(user=user)
        profile.save()
