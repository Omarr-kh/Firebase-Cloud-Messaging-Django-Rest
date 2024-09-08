from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications"
    )
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


class NotificationCount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)


class FirebaseDeviceToken(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="device_tokens"
    )
    token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
