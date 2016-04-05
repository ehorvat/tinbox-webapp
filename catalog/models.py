from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)
    rounded = models.BooleanField()
    rounded_cost = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):              # __unicode__ on Python 2
        return self.category_name

class Product(models.Model):
    category = models.ForeignKey(Category)
    product_dimensions = models.CharField(max_length=200)
    colors = models.ManyToManyField('customs.Color', blank=True)
    quantities = models.ManyToManyField('customs.Quantity', blank=True)
    turnarounds = models.ManyToManyField('customs.Shipping', blank=True)
    finishes = models.ManyToManyField('customs.Finish', blank=True)
    product_image = models.ImageField(upload_to='static/images/')
    rounded = models.BooleanField()
    rounded_cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.category.category_name
