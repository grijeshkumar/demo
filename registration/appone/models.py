from django.db import models

# Create your models here.

class Address(models.Model):

    address_1 = models.CharField(max_length=40)
    address_2 = models.CharField(max_length=40)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
