from django.contrib import admin

# Register your models here.
from apps.ratings.models import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ["buyer", "seller", "rating"]
    search_fields = ["seller__phone_number", "rating"]
