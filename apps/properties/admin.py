from django.contrib import admin

# Register your models here.
from apps.properties.models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'text']
