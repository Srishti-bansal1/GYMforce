from django.db import models

# Create your models here.
class EMmodel(models.Model):
    name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    email = models.EmailField()
    password = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100 )
    
class Loginuser(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    