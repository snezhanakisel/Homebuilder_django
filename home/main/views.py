from django.shortcuts import render
from .models import Carusel, Category, Mission
from project.models import *
from team.models import *
from .forms import ContactForm, FeedbackForm
from django.contrib import messages

# Create your views here.

menu = {
    'Home': 'home',
    'About': 'about',
    'Our team': 'team',
    'Project': 'project',
    'Blog': 'blog',
    'Contact': 'contact'
}
social_nerwork = {

}

def index(request):
    if request.method == 'POST':
        feedback = FeedbackForm(request.POST)
        if feedback.is_valid():
            feedback.save()


    carusel = Carusel.objects.all()
    cat = Category.objects.all()
    mission = Mission.objects.all()
    order = Project.objects.all()[:6]
    feedback = FeedbackForm

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
        'welcome': 'Welcome to Home Builder',
        'create': 'We create and turn into reality',
        'far': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia',
        'cats': cat,
        'missions': mission,
        'menu': menu,
        'facebook': 'https://www.facebook.com/TheElonmus',
        'twitter': 'https://twitter.com/elonmusk',
        'instagram': 'https://www.instagram.com/elonrmuskk/',
        'orders': order,
        'for_contact': 'Contact',
        'city': 'London',
        'adres': 'St. Liberty, 15',
        'tel': '8-015-321-654',
        'feedbacks': feedback,
    }
    return render(request, 'main/index.html', data)


def project(request):
    if request.method == 'POST':
        feedbacks = FeedbackForm(request.POST)
        if feedbacks.is_valid():
            feedbacks.save()

    order = Project.objects.all()
    feedbacks = FeedbackForm
    data = {
        'orders': order,
        'menu': menu,
        'facebook': 'https://www.facebook.com/TheElonmus',
        'twitter': 'https://twitter.com/elonmusk',
        'instagram': 'https://www.instagram.com/elonrmuskk/',
        'construction': 'Construction',
        'renovation': 'House Renovation',
        'painting': 'Painting',
        'design': 'Architecture Design',
        'for_contact': 'Contact',
        'city': 'London',
        'adres': 'St. Liberty, 15',
        'tel': '8-015-321-654',
        'feedbacks': feedbacks
    }
    return render(request, 'main/project.html', data)


def about(request):
    if request.method == 'POST':
        feedback = FeedbackForm(request.POST)
        if feedback.is_valid():
            feedback.save()

    feedback = FeedbackForm
    data = {
        'menu': menu,
        'facebook': 'https://www.facebook.com/TheElonmus',
        'twitter': 'https://twitter.com/elonmusk',
        'instagram': 'https://www.instagram.com/elonrmuskk/',
        'construction': 'Construction',
        'renovation': 'House Renovation',
        'painting': 'Painting',
        'design': 'Architecture Design',
        'for_contact': 'Contact',
        'city': 'London',
        'adres': 'St. Liberty, 15',
        'tel': '8-015-321-654',
        'feedbacks': feedback
    }
    return render(request, 'main/about.html', data)


def team(request):
    if request.method == 'POST':
        feedback = FeedbackForm(request.POST)
        if feedback.is_valid():
            feedback.save()

    employee = Employee.objects.all()
    feedback = FeedbackForm
    data = {
        'menu': menu,
        'facebook': 'https://www.facebook.com/TheElonmus',
        'twitter': 'https://twitter.com/elonmusk',
        'instagram': 'https://www.instagram.com/elonrmuskk/',
        'construction': 'Construction',
        'renovation': 'House Renovation',
        'painting': 'Painting',
        'design': 'Architecture Design',
        'for_contact': 'Contact',
        'city': 'London',
        'adres': 'St. Liberty, 15',
        'tel': '8-015-321-654',
        'employees': employee,
        'feedbacks': feedback
    }
    return render(request, 'main/team.html', data)


def contact_us(request):

    if request.method == 'POST' and 'Sendmessage' in request.POST:
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            messages.success(request, 'Thank you for message')
    if request.method == 'POST' and 'Send' in request.POST:
        feedback = FeedbackForm(request.POST)
        if feedback.is_valid():
            feedback.save()

    contact = ContactForm
    feedback = FeedbackForm

    data = {
        'menu': menu,
        'facebook': 'https://www.facebook.com/TheElonmus',
        'twitter': 'https://twitter.com/elonmusk',
        'instagram': 'https://www.instagram.com/elonrmuskk/',
        'construction': 'Construction',
        'renovation': 'House Renovation',
        'painting': 'Painting',
        'design': 'Architecture Design',
        'for_contact': 'Contact',
        'contact': contact,
        'city': 'London',
        'adres': 'St. Liberty, 15',
        'tel': '8-015-321-654',
        'email': 'builder@gmail.com',
        'website': 'homebuilder.com',
        'feedbacks': feedback

    }
    return render(request, 'main/contact.html', data)

