from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activity_type

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Notification(models.Model):
    sender = models.ForeignKey(User, related_name='dashboard_sent_notifications', on_delete=models.CASCADE, default=1)  # Provide a default value
    receiver = models.ForeignKey(User, related_name='dashboard_received_notifications', on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    is_broadcast = models.BooleanField(default=False)  # Add the is_broadcast field

    def __str__(self):
        return f'Notification from {self.sender.username} to {self.receiver.username if self.receiver else "All"}'
    
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dashboard_tasks')  # Adjusted related_name
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
