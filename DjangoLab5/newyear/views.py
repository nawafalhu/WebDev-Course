from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now()
    return render(request, r"D:\Code\DjangoLab5\newyear\templates\index.html", {
        'newyear': now.month == 1 and now.day == 1
    })