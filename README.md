
# Department Collaboration Platform

## Overview

The Department Collaboration Platform is a comprehensive web application designed to enhance communication, task management, and document storage within an organization. Built with Django, this platform supports user authentication, personalized dashboards, and seamless task tracking among staff members.

## Features

- **User Management**: Secure user authentication and personalized profiles.
- **Task Management**: Allows department heads to assign and track tasks, ensuring clear responsibilities and deadlines.
- **Automatic Notifications**: Sends reminders for task deadlines and calendar events directly to users' dashboards.
- **Document Storage**: Facilitates secure document uploads and organization for each user.
- **Knowledge Base**: A centralized repository for shared information and guidelines to promote collaboration and learning.
- **Specialized Admin Panel**: An in-built admin interface for easy management of users, tasks, and notifications.

## Installation

### Prerequisites

- Python 3.12 or higher
- Django 5.0 or higher
- MySQL or other database setup

### Steps to Install

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd Department-Collaboration-Platform
2. Create virtual environment
 ```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

3.Set up your database and update settings.py with your database configuration.

4.
```bash
python manage.py migrate

5.```bash
python manage.py createsuperuser

6.```bash
python manage.py runserver

7.
```bash
pip install django-crontab

8.INSTALLED_APPS = [
    ...
    'django_crontab',
]

CRONJOBS = [
    ('*/1 * * * *', 'django.core.management.call_command', ['send_reminders']),
]

9.```bash
python manage.py crontab add





#Acknowledgments
Built with Django Framework
Inspired by the need for efficient collaboration tools in departmental environments


Feel free to modify any sections or add more information as needed!
