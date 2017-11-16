from django.contrib import admin

# Register your models here.
from apps.category_product.models import CategoryProduct


@admin.register(CategoryProduct)
class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ["category","product"]