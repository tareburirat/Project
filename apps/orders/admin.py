from django.contrib import admin

# Register your models here.
from apps.orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'buyer', 'seller', 'product', 'price', 'date']
    search_fields = ['id', 'date']
