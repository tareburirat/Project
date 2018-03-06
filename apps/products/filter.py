import django_filters
from django.utils import timezone

from apps.products.models import Product


class ProductFilter(django_filters.rest_framework.FilterSet):
    promoted = django_filters.BooleanFilter(label='Promoted', method='promotion_filter')

    class Meta:
        model = Product
        fields = ['seller_id', 'product_status']

    def promotion_filter(self, queryset, name, value):
        if value is True:
            return queryset.filter(exp_date_promotion__gte=timezone.now()).order_by('exp_date_promotion')
        else:
            return queryset
