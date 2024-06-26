# admin_panel/admin.py

from django.contrib import admin
from .models import Task, Notification
# from django.contrib.admin import AdminSite

# class CustomAdminSite(AdminSite):
#     site_header = 'UniCon'
#     site_title = 'Admin Portal'

# admin.site = CustomAdminSite()


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

