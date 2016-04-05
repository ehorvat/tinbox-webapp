from django.contrib import admin
from .models import Color, Quantity, Shipping, Finish
# Register your models here.
admin.site.register(Color)
admin.site.register(Quantity)
admin.site.register(Shipping)
admin.site.register(Finish)
