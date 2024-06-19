from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images')
    desc = models.TextField()
    price = models.IntegerField()
    clicks = models.IntegerField(default=0)

class Travel_courses(models.Model):
    coursename = models.CharField(max_length=100)
    img = models.ImageField(upload_to='courseimages')
    desc = models.TextField()
    link = models.URLField(max_length = 200)

class Tourism_courses(models.Model):
    coursename = models.CharField(max_length=100)
    img = models.ImageField(upload_to='courseimages')
    desc = models.TextField()
    link = models.URLField(max_length=200)

class Hospitality_courses(models.Model):
    coursename = models.CharField(max_length=200)
    img = models.ImageField(upload_to='courseimages')
    desc = models.TextField()
    link = models.URLField(max_length=200)

class Hotel(models.Model):
    pic = models.ImageField(upload_to='hotelimages')
    name = models.CharField(max_length=300)
    rating = models.CharField(max_length=300)
    hprice = models.CharField(max_length=300)

class UserDestinations(models.Model):
    username = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    hotel = models.CharField(max_length=300)
    price = models.CharField(max_length=300)
    date = models.DateField()
