from django.shortcuts import render
from .models import Carusel

# Create your views here.


def index(request):
    carusel = Carusel.objects.all()
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

    }
    return render(request, 'main/index.html', data)
