# calendar_app/management/commands/send_reminders.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from calendar_app.models import CalendarEvent
from admin_panel.models import Notification

class Command(BaseCommand):
    help = 'Send reminders for upcoming calendar events'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        events = CalendarEvent.objects.filter(reminder_time__lte=now, reminder_time__gt=now - timezone.timedelta(minutes=1))
        for event in events:
            notification = Notification.objects.create(
                sender=event.user,
                receiver=event.user,
                message=f'Reminder: {event.title} is starting soon.'
            )
            notification.save()
            self.stdout.write(self.style.SUCCESS(f'Sent reminder for event {event.title}'))
