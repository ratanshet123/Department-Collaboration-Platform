from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'deadline', 'status')
    list_filter = ('user', 'deadline', 'status')
    search_fields = ('title', 'description')
