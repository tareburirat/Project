import django_filters
from django.utils import timezone

from apps.category_product.models import CategoryProduct


class CategoryProductFilter(django_filters.rest_framework.FilterSet):
    product_name = django_filters.CharFilter(name='product__name', lookup_expr='icontains', label='Product Name')
    promoted = django_filters.BooleanFilter(label='Promoted', method='promotion_filter')

    class Meta:
        model = CategoryProduct
        fields = ['product_name', 'category']

    def promotion_filter(self, queryset, name, value):
        if value is True:
            return queryset.filter(product__exp_date_promotion__gte=timezone.now()).order_by('product__exp_date_promotion')
        else:
            return queryset
