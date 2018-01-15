from rest_framework import serializers

from apps.category_product.models import CategoryProduct
from apps.products.serializers import ProductSerializer


class CategoryProductSerializer(serializers.ModelSerializer):
    product_data = serializers.SerializerMethodField()

    class Meta:
        model = CategoryProduct
        fields = [
            'category',
            'product',
            'product_data'
        ]

    def get_product_data(self, obj):
        return ProductSerializer(obj.product).data