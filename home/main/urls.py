from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('project/', project, name='project'),
    path('about/', about, name='about'),
    path('team/', team, name='team'),
    path('contact/', contact_us, name='contact_us'),

]