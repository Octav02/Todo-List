from django.shortcuts import redirect, render
from .models import Task
from .forms import TaskForm

def home(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'todo/home.html',context)

def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()

    context = {'form': form}
    return render(request, 'todo/create.html', context)
    
def update(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    context = {'form': form}
    return render(request, 'todo/update.html', context)

def delete(request, pk):
    task = Task.objects.get(pk=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('home')

    return render(request, 'todo/delete.html', {'task': task})