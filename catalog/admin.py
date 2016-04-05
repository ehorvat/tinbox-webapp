from django.contrib import admin
from customs.models import Shipping, Quantity, Color
from .models import Category, Product

# Register your models here.

class ColorInline(admin.TabularInline):
    model = Color
    extra = 1

class ShippingInline(admin.TabularInline):
    model = Shipping
    extra = 1

class QuantityInline(admin.TabularInline):
    model = Quantity
    extra = 1

class ProductInline(admin.TabularInline):
    list_display = ('product_name', 'id')
    model = Product
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'view_link')
    list_select_related = True
    def view_link(self, obj):
      return u'<a href="/admin/catalog/product/?category__id__exact=%s">View Subproducts</a>' % (obj.id)
    view_link.short_description = ''
    view_link.allow_tags = True

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_dimensions', 'category')
    list_filter = ('category',)



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
