from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from PIL import Image
from events.models import Event
from organizations.models import Club
# from django_mysql.models import ListCharField
# Create your models here.
#from django_mysql.models import JSONField


class Profile(models.Model):
    id = models.IntegerField(default=0,primary_key=True,unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name="email", max_length=60, default=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    subscriptions = models.ManyToManyField(Club)
    events = models.ManyToManyField(Event)
    #schedule = JSONField()
    tags = models.TextField(default="No Tags")

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


"""
class AccountManager(BaseUserManager):
    def createUser(self, email, username, password=None):
        if not email:
            raise ValueError("Users are required to have their email.")
        if not username:
            raise ValueError("Users are required to have a username")
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def createSuperUser(self, email, username, password):
        user = self.createUser(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_Admin = True
        user.is_Staff = True
        user.is_superUser = True
        user.save(using=self.db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    userName = models.CharField(max_length=60, unique=True)
    # schedule
    school = models.CharField(max_length=3)
    graduationYear = models.IntegerField()
    # achievements
    tags = models
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AccountManager()

    def __str__(self):
        return self.userName + ", " + self.email

    def has_permission(self, permission, obj=None):
        return self.is_admin

    def has_module_permissions(self, app_label):
        return True
"""
