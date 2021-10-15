from django.shortcuts import render
from .models import Carusel, Category, Mission, Feedback
from project.models import *
from team.models import Employee
from .forms import ContactForm, FeedbackForm, MailForm
from django.contrib import messages
from blog.models import Post


# Create your views here.


def index(request):

    if request.method == 'POST' and 'Subscribe' in request.POST:
        mail = MailForm(request.POST)
        if mail.is_valid():
            mail.save()
            messages.success(request, 'Thank you for message')

    if request.method == 'POST' and 'Send' in request.POST:
        feed = FeedbackForm(request.POST)
        if feed.is_valid():
            feed.save()

    # if request.method == 'POST':
    #     feed = FeedbackForm(request.POST)
    #     if feed.is_valid():
    #         feed.save()

    carusel = Carusel.objects.all()
    cat = Category.objects.all()
    mission = Mission.objects.all()
    order = Project.objects.all()[:6]
    feed = FeedbackForm
    feedback = Feedback.objects.all()
    mail = MailForm
    post = Post.objects.all()[:3]

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
        'cat': cat,
        'mission': mission,
        'facebook': 'https://www.facebook.com/TheElonmus',
        'twitter': 'https://twitter.com/elonmusk',
        'instagram': 'https://www.instagram.com/elonrmuskk/',
        'orders': order,
        'for_contact': 'Contact',
        'city': 'London',
        'adres': 'St. Liberty, 15',
        'tel': '8-015-321-654',
        'feed': feed,
        'feedbacks': feedback,
        'mail': mail,
        'post':post

    }
    return render(request, 'main/index.html', data)


def project(request):
    if request.method == 'POST':
        feed = FeedbackForm(request.POST)
        if feed.is_valid():
            feed.save()

    order = Project.objects.all()
    feed = FeedbackForm
    data = {
        'orders': order,
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
        'feed': feed
    }
    return render(request, 'main/project.html', data)


def about(request):

    if request.method == 'POST':
        feed = FeedbackForm(request.POST)
        if feed.is_valid():
            feed.save()

    feed = FeedbackForm
    cat = Category.objects.all()
    mission = Mission.objects.all()
    order = Project.objects.all()[:6]
    feedback = Feedback.objects.all()
    data = {
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
        'feed': feed,
        'cat': cat,
        'mission': mission,
        'orders': order,
        'feedbacks': feedback
    }
    return render(request, 'main/about.html', data)


def team(request):

    if request.method == 'POST':
        feed = FeedbackForm(request.POST)
        if feed.is_valid():
            feed.save()

    employee = Employee.objects.all()
    feed = FeedbackForm
    data = {
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
        'feed': feed
    }
    return render(request, 'main/team.html', data)


def contact_us(request):

    if request.method == 'POST' and 'Sendmessage' in request.POST:
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            messages.success(request, 'Спасибо за ваше сообщение!')
        else:
            messages.warning(request, 'Проверьте пожалуйста вводимую информацию!')

    if request.method == 'POST' and 'Send' in request.POST:
        feed = FeedbackForm(request.POST)
        if feed.is_valid():
            feed.save()

    contact = ContactForm
    feed = FeedbackForm

    data = {
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
        'feed': feed

    }
    return render(request, 'main/contact.html', data)




