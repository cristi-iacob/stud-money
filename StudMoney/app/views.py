from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from StudMoney.forms import SignUpForm, AddTaskForm
from app.models import Task, AcceptedTasks

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

    return render(request, 'view_tasks.html', context)

def view_posted_tasks(request):
    user = request.user
    context = {
        'tasks': Task.objects.all().filter(owner=user),
        'title': 'Your tasks'
    }

    return render(request, 'view_posted_tasks.html', context)

def view_accepted_tasks(request):
    user = request.user
    accepted_tasks = AcceptedTasks.objects.filter(user=user)
    tasks = []

    for accepted_task in accepted_tasks:
        for task in Task.objects.all():
            if accepted_task.task == task:
                tasks.append(task)
    context = {
        'tasks': tasks,
        'title': 'Your accepted tasks'
    }

    return render(request, 'view_tasks.html', context)
