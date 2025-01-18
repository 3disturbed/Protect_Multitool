from django.db import models
from django.contrib.auth.models import User
import random

# Create your models here.

class PlannedRoute(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='planned_routes')
    starting_location = models.CharField(max_length=200, verbose_name="Starting Location", help_text="Where are you starting from?")
    finishing_location = models.CharField(max_length=200, verbose_name="Finishing Location", help_text="Where are you going?")
    with_who = models.CharField(max_length=200, verbose_name="Companions", help_text="Who are you going with?")
    time_limit = models.PositiveIntegerField(verbose_name="Time Limit (Minutes)", help_text="Set a timer in minutes for safety.")
    pin_code = models.CharField(max_length=10, verbose_name="Pin Code", help_text="Alphanumeric pin code to confirm arrival or share if not safe.")
    additional_info = models.CharField(max_length= 1000, verbose_name="Additional information", help_text="Any further information that may be useful", blank=True, null=True)
    secret_key = models.CharField(
        max_length=10,
        default='',  # Placeholder
        editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Generate a random secret_key if not already set
        if not self.secret_key:
            self.secret_key = self.generate_secret_key()

        # Generate a random alphanumeric pin_code if not already set
        if not self.pin_code:
            self.pin_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

        super().save(*args, **kwargs)

    def generate_secret_key(self):
        # Generate a 6-digit random number as a string
        return str(random.randint(100000, 999999))

    def __str__(self):
        return f"Route by {self.user.username} from {self.starting_location} to {self.finishing_location}"

