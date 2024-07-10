from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import CalendarEvent
from .forms import CalendarEventForm

@login_required
def calendar_view(request):
    events = CalendarEvent.objects.filter(user=request.user).order_by('start_date')
    return render(request, 'calendar_app/calendar.html', {'events': events})

@login_required
def add_event(request):
    if request.method == 'POST':
        form = CalendarEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('calendar_view')
    else:
        form = CalendarEventForm()
    return render(request, 'calendar_app/add_event.html', {'form': form})

@login_required
def edit_event(request, event_id):
    event = CalendarEvent.objects.get(id=event_id, user=request.user)
    if request.method == 'POST':
        form = CalendarEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('calendar_view')
    else:
        form = CalendarEventForm(instance=event)
    return render(request, 'calendar_app/edit_event.html', {'form': form, 'event': event})
