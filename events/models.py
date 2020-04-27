from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from organizations.models import Club

from PIL import Image


class Event(models.Model):
    id = models.IntegerField(default=0, primary_key=True, unique=True)
    name = models.CharField(max_length=120, default='Untitled')  # length of title
    affiliation = models.TextField(default="No Affiliation")
    picture = models.ImageField(default='default.jpg', upload_to='event_banner', blank=True)
    description = models.TextField(default="Description Needed")  # info about event
    date = models.TextField(default="March 20, 2018")
    time = models.TextField(max_length=60, default="12:00:00")
    location = models.TextField(max_length=40, default='CAS')
    type = models.TextField(max_length=20, default="GENERAL_MEETING")
    tags = models.TextField(default="No Tags")
    contact = models.EmailField(verbose_name='email', max_length=60, default=False)
    affiliation_id = models.ForeignKey(to=Club, related_name='Events', on_delete=models.CASCADE, default=999)

    def save(self):
        super().save()

        img = Image.open(self.picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)

    def __str__(self):
        return self.name

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
