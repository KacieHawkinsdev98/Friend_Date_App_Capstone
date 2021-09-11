from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.Charfield(max_length=50)
    last_name = models.Charfield(max_length=50)
    phone_number = models.Integerfield()
    email = models.Charfield(max_length=50)
    username = models.Charfield(max_length=50)
    age = models.Integerfield()
    location = models.Locationfield()
    




