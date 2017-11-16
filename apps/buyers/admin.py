from django.contrib import admin

# Register your models here.
from apps.buyers.models import Buyer


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ["id","account","phone_number"]
