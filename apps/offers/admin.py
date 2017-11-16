from django.contrib import admin

# Register your models here.
from apps.offers.models import Offer


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
        list_display = ('id','offer_price','status','buyer','product')