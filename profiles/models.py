from django.db import models

# Create your models here.

class Profile(models.Model):
    user_name= models.CharField(max_length=100)
    name= models.CharField(max_length=100)
    