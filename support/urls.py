from django.urls import path
from .views import support_view

urlpatterns = [
    path('', support_view, name='support'),
]
