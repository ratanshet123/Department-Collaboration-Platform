from django.contrib import admin

from knowledge_base.models import Document
from .models import Task, Notification
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'deadline', 'completed')
    list_filter = ('user', 'deadline', 'completed')
    search_fields = ('title', 'description')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'message', 'timestamp', 'read')
    list_filter = ('sender', 'receiver', 'timestamp', 'read')
    search_fields = ('message', 'sender__username', 'receiver__username')

# Unregister the original User admin.
admin.site.unregister(User)
admin.site.register(Document)

# Register the new User admin.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass
