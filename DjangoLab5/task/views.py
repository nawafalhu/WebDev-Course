from django.shortcuts import render

tasks = ['task1', 'task2', 'task3']
# Create your views here.

def index(request):
    return render(request, r"D:\Code\DjangoLab5\task\templates\tasks\index.html", {
        "tasks":tasks
    })

def add(request):
    return render(request, r"D:\Code\DjangoLab5\task\templates\tasks\add.html")