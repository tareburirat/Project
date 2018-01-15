import django_filters

from apps.category_product.models import CategoryProduct


class CategoryProductFilter(django_filters.rest_framework.FilterSet):
    product_name = django_filters.CharFilter(name='product__name', lookup_expr='icontains', label='Product Name')

    class Meta:
        model = CategoryProduct
        fields = ['product_name', 'id']
