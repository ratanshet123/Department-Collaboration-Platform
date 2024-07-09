from django.urls import path
from .views import integrations_view

urlpatterns = [
    path('', integrations_view, name='integrations'),
]
