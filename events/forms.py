from django import forms
from .models import Event



class createEvent():

    class Meta:
        model = Event
        fields = ('title','content')