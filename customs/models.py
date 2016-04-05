from django.db import models
from catalog.models import Product

# Create your models here.
class Finish(models.Model):
    finish = models.CharField(max_length=200)
    finish_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    #@property
    #def total_cost(self):
        #return self.quantity * self.product.cost_per_unit

    def __str__(self):              # __unicode__ on Python 2
        return str(self.finish)

class Quantity(models.Model):
    quantity = models.IntegerField()
    quantity_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    #@property
    #def total_cost(self):
        #return self.quantity * self.product.cost_per_unit

    def __str__(self):              # __unicode__ on Python 2
        return str(self.quantity) + " - $" + str(self.quantity_cost)


class Shipping(models.Model):
    turnaround = models.CharField(max_length=200)
    turnaround_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    def __str__(self):              # __unicode__ on Python 2
        return self.turnaround


class Color(models.Model):
    color = models.CharField(max_length=200)
    color_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    def __str__(self):              # __unicode__ on Python 2
        return self.color
