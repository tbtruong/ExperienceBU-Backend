from django.db import models
from django.utils import timezone
#from events.models import Event
from PIL import Image


# from django.contrib.auth.models import User
# from userAccount.models import Account as User
# Create your models here.


class Club(models.Model):
    """
    clubId = models.CharField(max_length=10)
    clubName = models.CharField(max_length=30)
    clubPicture = models.ImageField(default='default.jpg')
    clubDescription = models.TextField(default="No Description")
    #clubMeetingTime = models.TimeField(default=timezone.now())
    clubRequirements = models.TextField(default="None")
    clubLocation = models.CharField(max_length=20,default="CAS 211")
    clubPersonOfContact = models.TextField(default="ryli1998@bu.edu")
    clubTags = models.TextField(default="No Tags")
    """
    id = models.IntegerField(default=0, primary_key=True, unique=True)
    name = models.CharField(max_length=30)
    picture = models.ImageField(default='default.jpg', upload_to='organization_banner', blank=True)
    description = models.TextField(default="Are there any descriptions?")
    # clubMeetingTime = models.TimeField(default=timezone.now())
    requirements = models.TextField(default="None")
    eboard = models.TextField(default="Bob Dole")
    time = models.TextField(default="12:00:00")
    location = models.TextField(default="CAS 211")
    contact = models.TextField(default="busmashbrosociety@gmail.com")
    tags = models.TextField(default="No Tags")
    #event_list = models.ForeignKey("events.Event", on_delete=models.CASCADE, related_name='clubs',default=)

    def save(self):
        super().save()

        img = Image.open(self.picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)

    def __str__(self):
        return self.name
