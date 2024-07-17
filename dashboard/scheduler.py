# dashboard/scheduler.py

import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from django.utils import timezone
from dashboard.models import Task, Notification
from django.contrib.auth.models import User

def send_task_notifications():
    now = timezone.now()
    tasks = Task.objects.filter(deadline__lte=now, completed=False)
    for task in tasks:
        Notification.objects.create(
            sender=User.objects.get(username='admin'),  # Assuming admin sends notifications
            receiver=task.user,
            message=f'Task "{task.title}" is past its deadline!',
            is_broadcast=False
        )

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        send_task_notifications,
        trigger=IntervalTrigger(minutes=1),
        id='send_task_notifications',
        name='Send task notifications every minute',
        replace_existing=True,
    )
    scheduler.start()
