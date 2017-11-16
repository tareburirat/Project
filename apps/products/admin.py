from django.contrib import admin

# Register your models here.
from apps.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
        list_display = ('id','status','date_of_sale','seller')