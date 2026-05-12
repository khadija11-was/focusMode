from django.shortcuts import render, redirect
from .models import Task
from django.views.decorators.csrf import csrf_exempt



def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': tasks})

@csrf_exempt
def add_task(request):
    if request.method == "POST":
        Task.objects.create(title=request.POST['title'])
    return redirect('task_list')


def delete_task(request, id):
    Task.objects.get(id=id).delete()
    return redirect('task_list')