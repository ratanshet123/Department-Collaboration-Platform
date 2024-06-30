from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    status_choices = [
        ('incomplete', 'Incomplete'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='incomplete')
    document = models.FileField(upload_to='task_documents/', blank=True, null=True)

    def __str__(self):
        return self.title
