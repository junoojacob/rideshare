from django.conf import settings
from django.db import models

class Ride(models.Model):
    """
    Creates Ride DataBase
    """
    STATUS_CHOICES = (
        ('requested', 'Requested'),
        ('started', 'Started'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    rider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rides_as_rider')
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='rides_as_driver')
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='requested')
    current_location = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ride {self.id} - {self.status}"