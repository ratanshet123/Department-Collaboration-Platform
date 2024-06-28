from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskUpdateForm

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-deadline')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskUpdateForm(instance=task)
    return render(request, 'tasks/task_update.html', {'form': form, 'task': task})
