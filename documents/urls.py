from django.urls import path
from .views import document_list

urlpatterns = [
    path('documents/', document_list, name='document_list'),
]
