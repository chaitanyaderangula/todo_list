from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('-id')
    form = TaskForm()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)

@require_POST
def add_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        new_task = Task(title=request.POST['title'])
        new_task.save()
    return redirect('index')

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('index')

def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = True
    task.save()
    return redirect('index')
