from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save
from django.conf import settings



# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)
    profile = models



 

class Match(models.Model):
   match_id = models.CharField(max_length=50)
   timestamp = models.TimeField()
   user_id = models.CharField(max_length=50)

   
    
class Pictures(models.Model):
  picture_id = models.IntegerField()
  user_id =  models.CharField(max_length=50)


class Likes(models.Model):
  user_id = models.CharField(max_length=50)
  liked_user = models.CharField(max_length=50)



class Dislikes(models.Model):
  user_id = models.CharField(max_length=50)
  disliked_user = models.CharField(max_length=50)
  


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.CharField(max_length=500, blank=True)
  profile_id = models.IntegerField()
  image = models.ImageField('default.jpg', upload_to='profile_pics')
  friends = models.ManyToManyField("Profile", blank=True)

  def __str__(self):
     return f'{self.user.username} Profile'


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass

post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)

class FriendRequest(models.Model):
   to_user= models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)
   from_user= models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)
   timestamp= models.DateTimeField(auto_now_add=True)








class Location(models.Model):
  location_id = models.IntegerField()
  latitude = models.IntegerField()
  longitude = models.IntegerField()










    #gender_preference = models.CharField(max_length=50)
    #phone_number = models.IntegerField()
    #likes = models.IntegerField()
    #match_id =models.CharField(max_length=50)
    #interests = models.CharField(max_length=50)
    #food_preferences = models.CharField(max_length=50)
    #music_preferences = models.CharField(max_length=50)