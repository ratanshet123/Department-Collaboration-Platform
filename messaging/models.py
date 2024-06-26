# messaging/models.py

from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender} to {self.receiver} - {self.timestamp}"

class Notification(models.Model):
    sender = models.ForeignKey(User, related_name='messaging_sent_notifications', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='messaging_received_notifications', on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_broadcast = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification from {self.sender} to {self.receiver or 'All Users'} - {self.timestamp}"