# Department Collaboration Platform
## Images

![User Login - Profile 1 - Microsoft​ Edge 17-07-2024 20_10_15](https://github.com/user-attachments/assets/ff0b29f6-158a-42f0-b088-42e193dbe764)
![User Login - Profile 1 - Microsoft​ Edge 17-07-2024 20_10_33](https://github.com/user-attachments/assets/748f5894-3483-4ddd-b281-e52d92e455b7)
![User Login - Profile 1 - Microsoft​ Edge 17-07-2024 20_10_51](https://github.com/user-attachments/assets/d26cc849-cb0a-4783-a6ed-863b86984078)
![User Login - Profile 1 - Microsoft​ Edge 17-07-2024 20_10_59](https://github.com/user-attachments/assets/62a19659-8536-4d7c-a571-a3698e91f98a)
![User Login - Profile 1 - Microsoft​ Edge 17-07-2024 20_11_06](https://github.com/user-attachments/assets/c0b9e5fb-6340-4a82-b5c5-db3958afa096)


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
source env/bin/activate0
# On Windows use `env\Scripts\activate`


3.Set up your database and update settings.py with your database configuration.

4.
python manage.py migrate

5.
python manage.py createsuperuser

6.
python manage.py runserver

7.

pip install django-crontab

8.INSTALLED_APPS = [
    ...
    'django_crontab',
]

CRONJOBS = [
    ('*/1 * * * *', 'django.core.management.call_command', ['send_reminders']),
]

9.
python manage.py crontab add

__________________________________________________________________________________________________________________________

## Installation
-Built with Django Framework
-Inspired by the need for efficient collaboration tools in departmental environments


-Feel free to modify any sections or add more information as needed!




