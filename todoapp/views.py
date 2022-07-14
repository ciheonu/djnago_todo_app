from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TaskForm
from . models import Task


@login_required(login_url='login')
def home(request):
    user_id = request.user.id
    todo = Task.objects.filter(user_id=user_id).order_by('-id')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            messages.success(request, f'Task Added Successfully ! ')
            return redirect('home')
    else:
        form = TaskForm()
    context = {
        'todos': todo,
        'form': form
    }
    return render(request, 'task.html', context)


@login_required(login_url='login')
def delete(request, pk):
    todo = Task.objects.filter(user_id=request.user).get(id=pk)
    todo.delete()
    messages.success(request, f'Task Delete Successfully ! ')
    return redirect('home')


@login_required(login_url='login')
def update(request, pk):
    todo = Task.objects.filter(user_id=request.user).get(id=pk)
    update_form = TaskForm(instance=todo)
    if request.method == 'POST':
        update_form = TaskForm(request.POST, instance=todo)
        if update_form.is_valid():
            new_task = update_form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            messages.success(request, f'Task Edited Successfully ! ')
            return redirect('home')
    context = {
        'form': update_form
    }
    return render(request, 'task.html', context)


