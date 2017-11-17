from django.contrib import admin

# Register your models here.
from apps.products.models import Product, ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','status','date_of_sale','seller', 'freight', 'freight_detail_choices')


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'sequence', 'image_tag')
