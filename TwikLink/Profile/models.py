
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from colorfield.fields import ColorField
import requests,random,string
from django.core.files.base import ContentFile

class Profile(models.Model):
    GradientOptions = [
        ("to top","Top"),
        ("to right top","Right top"),
        ("to right","Right"),
        ("to right bottom","Right bottom"),
        ("to bottom","Bottom"),
        ("to left bottom","Left bottom"),
        ("to left","Left"),
        ("to left top","Left top"),
    ]
    username = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    verifyUser = models.BooleanField(default=False)
    # colorUser = models.CharField(max_length=6, null=True,blank=True,)
    Description = models.TextField(blank=True,null=True)
    colorDescription = ColorField(default='#ffffff',null=True,blank=True,format='hex')
    photoProfile = models.CharField(null=True,blank=True)
    # photoProfile = models.ImageField(upload_to='PhotoProfiles/' ,height_field=None, width_field=None, max_length=None, null=True,blank=True)
    BackgroundProfile = models.ImageField(default='/asstes/images/backgroundProfile.jpg',upload_to='BackgroundProfiles/', height_field=None, width_field=None, max_length=None, null=True,blank=True)
    BackgroundBlur = models.IntegerField(blank=True, null=True,default=8)
    gradientActive = models.BooleanField(default=True)
    gradientOne = ColorField(default="#ffffff",null=True,blank=True,format='hex')
    gradientTwo = ColorField(default="#4dffff",null=True,blank=True,format='hex')
    gradientoption = models.CharField(max_length=30,null=True, blank=True,choices=GradientOptions,default='to top')
    tiktokURL = models.CharField(max_length=200,null=True, blank=True)
    instagramURL = models.CharField(max_length=200,null=True, blank=True)
    youtubeURL = models.CharField(max_length=200,null=True, blank=True)
    linkedinURL = models.CharField(max_length=200,null=True, blank=True)
    twitterURL = models.CharField(max_length=200,null=True, blank=True)
    FacebookURL = models.CharField(max_length=200,null=True, blank=True)
    GithubURL = models.CharField(max_length=200,null=True, blank=True)
    FirstName = models.CharField(max_length=30,null=True, blank=True)
    LastName = models.CharField(max_length=30,null=True, blank=True)
    Email = models.CharField(max_length=30,null=True, blank=True)
    PhoneNumber = models.CharField(max_length=30,null=True, blank=True)
    Address = models.CharField(max_length=200,null=True, blank=True)
    Country = models.CharField(max_length=200,null=True, blank=True)
    def __str__(self):
        return str(self.username)


class Item(models.Model):
    GradientOptions = [
        ("to top","Top"),
        ("to right top","Right top"),
        ("to right","Right"),
        ("to right bottom","Right bottom"),
        ("to bottom","Bottom"),
        ("to left bottom","Left bottom"),
        ("to left","Left"),
        ("to left top","Left top"),
    ]
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    text = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to='ItemPhotos/', height_field=None, width_field=None, max_length=None,null=True, blank=True)
    showPhoto = models.BooleanField(default=True)
    url = models.CharField(max_length=200,null=True,blank=True)
    backgroundbox = ColorField(default='#7a7a7a',null=True,blank=True,format='hex')
    backgoundActive = models.BooleanField(default=True)
    gradientOne = ColorField(default='#5558da',null=True,blank=True,format='hex')
    gradientTwo = ColorField(default='#5fd1f9',null=True,blank=True,format='hex')
    gradientoption = models.CharField(max_length=30,null=True, blank=True,choices=GradientOptions,default='to top')
    BackgroundBlur = models.IntegerField(blank=True, null=True,default=8)
    BackgroundBlurActive = models.BooleanField(default=True)
    def __str__(self):
        return str(self.user)
    

@receiver(post_save, sender=User)
def create_profile(sender,created,instance, **kwargs):
    if created:
        profile = Profile.objects.create(username=instance)
        url = "https://any-anime.p.rapidapi.com/v1/anime/png/1"
        headers = {
            "X-RapidAPI-Key": "5598a32debmshbb383db660e30f3p1dec56jsnce737093fa6e",
            "X-RapidAPI-Host": "any-anime.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            image_data = str(response.json()["images"][0])
            profile.photoProfile = image_data
            profile.save()


post_save.connect(create_profile, sender=User)
