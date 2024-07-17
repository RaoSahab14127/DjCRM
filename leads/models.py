from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
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
    
def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)