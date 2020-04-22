from django.shortcuts import render
from django.views.generic import ListView
from .models import Event
#from userAccount import Account as user
# Create your views here.


def show_events(request):
    request_instance = Event.objects.create()

