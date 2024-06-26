from django.urls import path
from . import views

urlpatterns = [
    path('', views.messaging_overview, name='messaging_overview'),
    path('inbox/', views.inbox, name='inbox'),
    path('sent_messages/', views.sent_messages, name='sent_messages'),
    path('send_message/', views.send_message, name='send_message'),
]
