from django.db import models

# Create your models here.
class firstapp(models.Model):

    origin_country = models.CharField(max_length=64)
    destnation_country = models.CharField(max_length=64)
    number_of_night = models.IntegerField()
    price = models.IntegerField()