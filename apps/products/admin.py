from django.contrib import admin

# Register your models here.
from apps.products.models import Product, ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'date_of_sale', 'seller', 'price', 'freight_fee', 'freight')


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'sequence', 'image_tag')
