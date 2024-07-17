# dashboard/management/commands/send_notifications.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from dashboard.models import Task, Notification
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Send notifications for tasks with upcoming deadlines'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        tasks = Task.objects.filter(deadline__lte=now, completed=False)
        for task in tasks:
            Notification.objects.create(
                sender=User.objects.get(username='admin'),  # Assuming admin sends notifications
                receiver=task.user,
                message=f'Task "{task.title}" is past its deadline!',
                is_broadcast=False
            )
        self.stdout.write(self.style.SUCCESS('Successfully sent notifications for tasks with upcoming deadlines'))
