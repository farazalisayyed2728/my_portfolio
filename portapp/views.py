from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

from django.shortcuts import render


def home(request):
    return render(request, 'portapp/home.html')


def about(request):
    return render(request, 'portapp/about.html')


def skills(request):
    return render(request, 'portapp/skills.html')


def projects(request):
    return render(request, 'portapp/projects.html')


def contact(request):
    return render(request, 'portapp/contact.html')