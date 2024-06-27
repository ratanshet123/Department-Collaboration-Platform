from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from admin_panel.models import Notification, Task


@login_required
def dashboard_view(request):
    user = request.user
    notifications = Notification.objects.filter(receiver=user).order_by('-timestamp')
    tasks = Task.objects.filter(user=user).order_by('-deadline')
    activities = []  # Define how to retrieve recent activities for the user
    return render(request, 'dashboard/dashboard.html', {
        'user': user,
        'notifications': notifications,
        'tasks': tasks,
        'activities': activities,
    })
