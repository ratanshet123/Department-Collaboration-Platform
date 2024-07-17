from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from admin_panel.models import Notification
from tasks.models import Task
from datetime import timedelta

@login_required
def dashboard_view(request):
    user = request.user
    
    # Create notifications for tasks due in the next 24 hours
    upcoming_tasks = Task.objects.filter(
        deadline__lte=timezone.now() + timedelta(days=1),
        user=user,
        status='incomplete'  # Use status instead of completed
    )
    
    for task in upcoming_tasks:
        Notification.objects.get_or_create(
            sender=user,
            receiver=user,
            message=f"Reminder: Your task '{task.title}' is due soon!",
        )

    notifications = Notification.objects.filter(receiver=user).order_by('-timestamp')
    tasks = Task.objects.filter(user=user).order_by('-deadline')
    activities = []  # Define how to retrieve recent activities for the user
    
    return render(request, 'dashboard/dashboard.html', {
        'user': user,
        'notifications': notifications,
        'tasks': tasks,
        'activities': activities,
    })

   