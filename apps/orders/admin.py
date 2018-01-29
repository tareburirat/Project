from django.contrib import admin

# Register your models here.
from apps.orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'buyer', 'price', 'date']
    search_fields = ['id', 'date']
