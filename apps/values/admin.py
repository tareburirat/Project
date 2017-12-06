from django.contrib import admin

# Register your models here.
from apps.values.models import Value


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'properties', 'value_product', 'properties_string']
    search_fields = ['id', 'product__name']