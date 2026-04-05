# INF601 - Advanced Programming in Python

# Kevin Vasquez

# Mini Project 4

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from .models import Expense, Category
from .forms import ExpenseForm, RegisterForm



def home(request):
    return render(request, 'tracker/home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})

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

@login_required
def categories(request):
    categories = Category.objects.filter(user=request.user)

    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Category.objects.create(name=name, user=request.user)
            return redirect('categories')

    return render(request, 'tracker/categories.html', {'categories': categories})


@login_required
def summary(request):
    expenses = Expense.objects.filter(user=request.user)

    total = sum(exp.amount for exp in expenses)

    return render(request, 'tracker/summary.html', {'total': total})


@login_required
def profile(request):
    total_expenses = Expense.objects.filter(user=request.user).count()
    total_categories = Category.objects.filter(user=request.user).count()

    return render(request, 'tracker/profile.html', {
        'total_expenses': total_expenses,
        'total_categories': total_categories
    })

@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)

    if request.method == 'POST':
        expense.delete()
        return redirect('dashboard')

    return redirect('dashboard')