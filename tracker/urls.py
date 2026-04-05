# INF601 - Advanced Programming in Python

# Kevin Vasquez

# Mini Project 4

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_expense, name='add_expense'),
]