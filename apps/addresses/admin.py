from django.contrib import admin

# Register your models here.
from apps.addresses.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
        list_display = ['id', 'buyer', 'address_details']
        search_fields = ['id', 'buyer__account__display_name']

