from django.urls import path
from .views import calendar_view, add_event, edit_event

urlpatterns = [
    path('', calendar_view, name='calendar_view'),
    path('add/', add_event, name='add_event'),
    path('edit/<int:event_id>/', edit_event, name='edit_event'),
]
