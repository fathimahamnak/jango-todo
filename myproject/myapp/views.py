from django.shortcuts import render,redirect

from .models import Task

def task_list(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('task_list')

    return render(request, 'task_list.html', {'tasks': tasks})

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('task_list')


# Create your views here.
