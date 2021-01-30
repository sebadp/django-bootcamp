from django.db import models

# Create your models here.

class Product(models.Model):
    title= models.CharField(max_length=100)
    description= models.CharField(max_length=300)
    price= models.IntegerField(default=0)
