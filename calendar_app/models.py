from django.db import models
from django.contrib.auth.models import User

class CalendarEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='calendar_events')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    reminder = models.BooleanField(default=False)

    def __str__(self):
        return self.title
