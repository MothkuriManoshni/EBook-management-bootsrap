from django.shortcuts import render, redirect
from .models import Task

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('home')

    tasks = Task.objects.all()
    return render(request, 'tasks/home.html', {'tasks': tasks})
def complete_task(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        task.completed = not task.completed
        task.save()
    return redirect('home')
def delete_task(request, task_id):
    if request.method == 'POST':
        Task.objects.get(id=task_id).delete()
    return redirect('home')