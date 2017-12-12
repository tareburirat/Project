from rest_framework import serializers

from apps.category_product.models import CategoryProduct


class CategoryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryProduct
        fields = [
            'category',
            'product'
        ]
