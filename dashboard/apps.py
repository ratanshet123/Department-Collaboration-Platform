# dashboard/apps.py

from django.apps import AppConfig

class DashboardConfig(AppConfig):
    name = 'dashboard'

    def ready(self):
        from .scheduler import start_scheduler
        start_scheduler()
