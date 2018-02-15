from django.contrib import admin

# Register your models here.
from apps.offers.models import Offer


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
        list_display = ['id', 'offer_price', 'offer_status', 'buyer', 'product']
        search_fields = ['id', 'account__username', 'product__name']
        list_filter = ['offer_status']
