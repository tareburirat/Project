from rest_framework import viewsets

from apps.category_product.models import CategoryProduct
from apps.category_product.serializers import CategoryProductSerializer


class CategoryProductViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer
    queryset = CategoryProduct.objects.all()