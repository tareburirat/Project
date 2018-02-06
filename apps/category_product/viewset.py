from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apps.category_product.filters import CategoryProductFilter
from apps.category_product.models import CategoryProduct
from apps.category_product.serializers import CategoryProductSerializer
from apps.products.models import Product


class CategoryProductViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer
    queryset = CategoryProduct.objects.filter(product__product_status=Product.sale)
    filter_class = CategoryProductFilter

