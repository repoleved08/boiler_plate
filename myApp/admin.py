from django.contrib import admin
from .models import Offer, Products

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'description', 'image')


class Product2Admin(admin.ModelAdmin):
    list_display = ('coupon', 'discount')


admin.site.register(Products, ProductAdmin)
admin.site.register(Offer, Product2Admin)
