from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)  # Added last name

    def __str__(self):
        return f"{self.first_name or self.user.username} {self.last_name or ''}'s Profile"


# Signal to automatically create/update the profile
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create the Profile only if first_name or last_name exists
        if instance.first_name or instance.last_name:
            profile = Profile.objects.create(user=instance)
            profile.first_name = instance.first_name
            profile.last_name = instance.last_name
            profile.save()
    else:
        # Update the Profile only if it already exists
        if hasattr(instance, 'profile'):
            profile = instance.profile
            profile.first_name = instance.first_name
            profile.last_name = instance.last_name
            profile.save()




