from django.contrib import admin

# Register your models here.
from django.db.models import Count, Sum

from apps.products.models import Product, ProductImage, ProductSummary


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product_status', 'date_of_sale', 'seller', 'price', 'freight_fee', 'freight',
                    'product_quality', 'detail')
    search_fields = ['id', 'name', 'seller__phone_number']
    list_filter = ['product_status']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'sequence', 'image_tag')


@admin.register(ProductSummary)
class ProductSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/sale_summary_change_list.html'
    date_hierarchy = 'date_of_sale'
    list_filter = ('product_status',)

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'total': Count('id'),
            'total_value': Sum('price'),
        }
        response.context_data['summary'] = list(
            qs
                .values('categoryproduct__category__name')
                .annotate(**metrics)
                .order_by('-total_value')
        )

        return response
