from django.contrib import admin

# Register your models here.
from apps.categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "category_type"]
    search_fields = ['id', 'name']
    list_filter = ['category_type']
