"""
URL configuration for a1_main_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# a1_main_project/urls.py

from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from home import views as home_views
from dashboard import views as dashboard_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts_views.login_view, name='login'), 
    path('accounts/', include('accounts.urls')), 
    path('home/', home_views.home, name='home'),  
    path('dashboard/', include('dashboard.urls')),  
    path('messaging/', include('messaging.urls')),
]
