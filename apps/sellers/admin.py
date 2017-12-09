from django.contrib import admin

# Register your models here.
from apps.sellers.models import Seller


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
        list_display = ('id', 'phone_number', 'expire_date', 'account', 'address')
        search_fields = ['id', 'account__username', 'phone_number']
