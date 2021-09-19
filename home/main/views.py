from django.shortcuts import render
from .models import Carusel, Category, Mission
from project.models import *

# Create your views here.


def index(request):
    carusel = Carusel.objects.all()
    cat = Category.objects.all()
    mission = Mission.objects.all()
    menu = {
        'Home': 'home',
        'About': 'about',
        'Our team': 'team',
        'Project': 'project',
        'Blog': 'blog',
        'Contact': 'contact'
    }

    data = {
        'carusels': carusel,
        'construction': 'Construction',
        'renovation': 'House Renovation',
        'painting': 'Painting',
        'design': 'Architecture Design',
        'description': 'Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic.',
        'expert': 'Expert & Professional',
        'work': 'High Quality Work',
        'help': '24/7 Help Support',
        'content': 'Separated they live in. A small river named Duden flows.',
        'cats': cat,
        'missions': mission,
        'menu': menu


    }
    return render(request, 'main/index.html', data)


def project(request):
    order = Project.objects.all()
    data1 = {
        'orders': order
    }
    return render(request, 'main/project.html', data1)


def about(request):
    return render(request, 'main/about.html')
