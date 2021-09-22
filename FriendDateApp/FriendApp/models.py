from django.db import models



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
    profile = models.CharField



 

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
  bio = models.CharField(max_length=500)
  profile_id = models.IntegerField()
  image = models.ImageField('default.jpg', upload_to='profile_pics')
  
  def __str__(self):
     return f'{self.user.username} Profile'






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