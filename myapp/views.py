
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask, CreateNewProject
# Create your views here.


def index(request):
    tittle = 'Django Course!!!'
    return render(request, 'index.html', {
        'tittle': tittle
    })


def about(request):
    username = 'Martin'
    return render(request, 'about.html', {
        'username': username
    })


def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })


def tasks(request):
    # task = Task.objects.get(tittle = tittle)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(
            tittle=request.POST['tittle'], description=request.POST['description'], project_id=1)
        return redirect('/tasks/')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        print(request.POST)
        project = Project.objects.create(name=request.POST["name"])
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
