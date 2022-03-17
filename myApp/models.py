from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    stock = models.IntegerField()
    description = models.CharField(max_length=2083)
    image = models.CharField(max_length=2083)

class Offer(models.Model):
    coupon = models.CharField(max_length=50)
    discount = models.FloatField()