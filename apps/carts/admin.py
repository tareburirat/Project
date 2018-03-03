from django.contrib import admin

from apps.carts.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'owner']
    search_fields = ['id']
