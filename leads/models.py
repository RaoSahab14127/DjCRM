from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.user.username}"
class Lead(models.Model):
    data  = (
        ('internet' , 'internet'),
        ('call', 'call'),
        ('sms', 'sms')
    )
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField(blank=False)
    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=data, max_length= 200)
    profilephoto = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    special_files = models.FileField(upload_to='special_files/', blank=True, null=True)
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"