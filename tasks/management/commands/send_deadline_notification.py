from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from tasks.models import Task
from notifications.models import Notification
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Send notifications for tasks with upcoming deadlines'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        upcoming_deadline = now + timedelta(days=1)
        tasks = Task.objects.filter(deadline__lte=upcoming_deadline, deadline__gte=now, status='incomplete')

        for task in tasks:
            Notification.objects.create(
                sender=User.objects.get(username='admin'),  # Adjust to the appropriate admin user
                receiver=task.user,
                message=f'Reminder: The deadline for your task "{task.title}" is approaching.'
            )

        self.stdout.write(self.style.SUCCESS('Successfully sent deadline notifications'))
