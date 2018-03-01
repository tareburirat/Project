from django.contrib import admin

# Register your models here.
from apps.orders.models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'buyer', 'price', 'date',]
    search_fields = ['id', 'date']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'order_status', 'order_track']
    search_fields = ['id', 'order_track']