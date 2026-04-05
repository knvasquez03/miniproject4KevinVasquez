# INF601 - Advanced Programming in Python

# Kevin Vasquez

# Mini Project 4

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracker.urls')),
]
