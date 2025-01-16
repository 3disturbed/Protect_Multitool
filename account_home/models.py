from django.db import models
from django.contrib.auth.models import User

class EmergencyContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emergency_contacts')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    relationship = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.relationship}) - {self.phone}"

