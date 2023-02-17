import requests
from django.db import models
from django.contrib.postgres.fields import JSONField

class Network(models.Model):
    company = models.CharField(max_length=1000)
    gbfs_href = models.CharField(max_length=1000)
    href = models.CharField(max_length=1000)
    id = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    country =models.CharField(max_length=1000)
    latitude= models.FloatField()
    longitude= models.FloatField()
    name = models.CharField(max_length=1000)

class Stations(models.Model):
        empty_slots= models.IntegerField()
        address = models.CharField(max_length=1000)
        altitude = models.FloatField()
        ebikes = models.IntegerField()
        has_ebikes= models.BooleanField()
        last_updated= models.IntegerField()
        normal_bikes = models.IntegerField()
        payment=models.CharField(max_length=1000)
        payment_terminal = models.BooleanField()
        post_code = models.IntegerField()
        renting = models.IntegerField()
        returning = models.IntegerField()
        slots = models.IntegerField()
        uid = models.IntegerField()
        free_bikes = models.IntegerField()
        id = models.CharField(max_length=1000)
        latitude =  models.FloatField()
        longitude =  models.FloatField()
        name =  models.models.CharField(max_length=1000)
        timestamp =  models.DateTimeField()
        



