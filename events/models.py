from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# from PIL import Image
# from userAccount.models import Account as User


class Event(models.Model):
    """
    eventID = models.CharField(max_length=20, unique=True)
    eventName = models.CharField(max_length=120, default='Untitled')  # length of title
    eventAffiliation = models.CharField(max_length=30, default="None")
    banner = models.ImageField(default='default.jpg')
    content = models.TextField(default="Description Needed")  # info about event
    # date_posted = models.DateTimeField(default=timezone.now) #when post was created
    eventTime = models.CharField(max_length=20, default="12:00:00")
    eventLocation = models.CharField(max_length=40, default='CAS')
    eventType = models.CharField(max_length=20,  default="GENERAL_MEETING")
    eventTags = models.TextField(default="No Tags")
    contact_info = models.EmailField(verbose_name='email', max_length=60, default=False)
    """
    id = models.IntegerField(default=0, primary_key=True, unique=True)
    name = models.CharField(max_length=120, default='Untitled')  # length of title
    affiliation = models.CharField(max_length=30, default="None")
    picture = models.ImageField(default='default.jpg')
    description = models.TextField(default="Description Needed")  # info about event
    date = models.TextField(default="March 20, 2018")
    time = models.CharField(max_length=20, default="12:00:00")
    location = models.CharField(max_length=40, default='CAS')
    type = models.CharField(max_length=20, default="GENERAL_MEETING")
    tags = models.TextField(default="No Tags")
    contact = models.EmailField(verbose_name='email', max_length=60, default=False)

    # alreadyHappened = models.BooleanField(default=True)

    def record(self):
        self.save()

    def __str__(self):
        return self.eventName
