from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from StudMoney.forms import SignUpForm, AddTaskForm
from app.models import Task

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            name = form.cleaned_data.get('name')
            starttime = form.cleaned_data.get('starttime')
            location = form.cleaned_data.get('location')
            description = form.cleaned_data.get('description')
            reward = float(form.cleaned_data.get('reward'))
            owner = request.user
            task = Task(owner=owner, name=name, starttime=starttime, location=location, description=description, reward=reward)
            task.save()
            return redirect('home')
    else:
        form = AddTaskForm()
    return render(request, "add_task.html", {'form': form})

def view_tasks(request):
    context = {
        'tasks': Task.objects.all(),
        'title': 'Tasks'
    }
    for task in Task.objects.all():
        print(task.id, task.owner, task.name, task.starttime, task.location, task.description, task.reward)
    return render(request, 'view_tasks.html', context)