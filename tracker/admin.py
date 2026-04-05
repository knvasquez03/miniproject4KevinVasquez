# INF601 - Advanced Programming in Python

# Kevin Vasquez

# Mini Project 4

from django.contrib import admin
from .models import Category, Expense


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name',)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'date', 'category', 'user')
    list_filter = ('date', 'category')
    search_fields = ('title', 'notes')
