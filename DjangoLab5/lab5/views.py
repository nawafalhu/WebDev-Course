from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, r"D:\Code\DjangoLab5\lab5\templates\index.html", {
        'name':'nawaf'
    })

def greet(request, name):
    return HttpResponse(f"hello {name}")