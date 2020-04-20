from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User
#from userAccount.models import Account as User
# Create your models here.


class Club(models.Model):
    clubId = models.CharField(max_length=10)
    clubName = models.CharField(max_length=30)
    clubPicture = models.ImageField(default='default.jpg')
    clubDescription = models.TextField()
    #clubMeetingTime = models.TimeField(default=timezone.now())
    clubLocation = models.CharField(max_length=20,default="CAS 211")
    clubPersonOfContact = models.TextField(default="Adam Garfield")
    clubTags = models.TextField(default="No Tags")
