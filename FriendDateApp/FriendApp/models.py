from django.db import models



# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50)
    age = models.IntegerField()
    #location = models.PointField(0, blank=0,)
    gender = models.CharField(max_length=50)
    gender_preference = models.CharField(max_length=50)
    likes = models.IntegerField()
    match_id =models.CharField(max_length=50)
    interests = models.CharField(max_length=50)
    food_preferences = models.CharField(max_length=50)
    music_preferences = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)


    def __str__(self):
      return self.name

class Match(models.Model):
   match_id = models.CharField(max_length=50)
   timestamp = models.TimeField()
   user_id = models.CharField(max_length=50)

   def __str__(self):
      return self.name

    
class Pictures(models.Model):
  picture_id = models.IntegerField()
  user_id =  models.CharField(max_length=50)

  def __str__(self):
      return self.name

class Likes(models.Model):
  user_id = models.CharField(max_length=50)
  liked_user = models.CharField(max_length=50)

  def __str__(self):
      return self.name

class Dislikes(models.Model):
  user_id = models.CharField(max_length=50)
  disliked_user = models.CharField(max_length=50)
  
  def __str__(self):
      return self.name

class Profiles(models.Model):
  profile_id = models.IntegerField()
  user_id = models.CharField(max_length=50)

  def __str__(self):
      return self.name

class Location(models.Model):
  location_id = models.IntegerField()
  latitude = models.IntegerField()
  longitude = models.IntegerField()

  def __str__(self):
      return self.name







