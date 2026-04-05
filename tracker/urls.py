# INF601 - Advanced Programming in Python

# Kevin Vasquez

# Mini Project 4

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_expense, name='add_expense'),
    path('categories/', views.categories, name='categories'),
    path('summary/', views.summary, name='summary'),
    path('profile/', views.profile, name='profile'),
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
]