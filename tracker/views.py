# INF601 - Advanced Programming in Python

# Kevin Vasquez

# Mini Project 4

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Expense, Category
from .forms import ExpenseForm


def home(request):
    return render(request, 'tracker/home.html')


@login_required
def dashboard(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    return render(request, 'tracker/dashboard.html', {'expenses': expenses})


@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        form.fields['category'].queryset = Category.objects.filter(user=request.user)

        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()
        form.fields['category'].queryset = Category.objects.filter(user=request.user)

    return render(request, 'tracker/add_expense.html', {'form': form})