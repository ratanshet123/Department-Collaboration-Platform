from django.shortcuts import render
from .models import Activity, Task, Notification

def dashboard_view(request):
    activities = Activity.objects.filter(user=request.user).order_by('-timestamp')[:10]
    tasks = Task.objects.filter(user=request.user, completed=False).order_by('deadline')[:10]
    # notifications = Notification.objects.filter(user=request.user, read=False).order_by('-timestamp')[:10]
    
    context = {
        'activities': activities,
        'tasks': tasks,
        # 'notifications': notifications
    }
    
    return render(request, 'dashboard/dashboard.html', context)
