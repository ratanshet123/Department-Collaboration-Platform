from django.urls import path
from .views import task_list, task_update

urlpatterns = [
    path('', task_list, name='task_list'),
    path('update/<int:pk>/', task_update, name='task_update'),
]
