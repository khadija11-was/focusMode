from django.shortcuts import render, redirect
from .models import Pomodoro
from tasks.models import Task

def pomodoro_list(request):
    pomodoros = Pomodoro.objects.all()
    tasks = Task.objects.all()

    return render(request, 'pomodoros/list.html', {
        'pomodoros': pomodoros,
        'tasks': tasks
    })


def add_pomodoro(request):
    if request.method == "POST":
        task = Task.objects.get(id=request.POST['tasks'])
        duration = request.POST['duration']

        Pomodoro.objects.create(task=task, duration=duration)

    return redirect('pomodoro_list')