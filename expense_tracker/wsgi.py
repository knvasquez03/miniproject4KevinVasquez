# INF601 - Advanced Programming in Python

# Kevin Vasquez

# Mini Project 4
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'expense_tracker.settings')

application = get_wsgi_application()
