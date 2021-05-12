from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        taskform = TaskForm(request.POST)
        if taskform.is_valid():
            taskform.save()
    inputForm = TaskForm()
    return render(request, 'task_list.html', {'tasks': tasks, 'inputForm': inputForm})

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.is_completed = True
        task.save()
    return redirect('/')

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
    return redirect('/')