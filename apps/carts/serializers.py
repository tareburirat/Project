from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers

from apps.carts.models import Cart
from apps.products.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    product_data = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        exclude = []
        filter_backends = (DjangoFilterBackend,)
        filter_fields = ['product_id', 'owner_id', 'in_cart']
        extra_kwargs = {
            'in_cart': {
                'initial': True
            }
        }

    def get_product_data(self, obj):
        return ProductSerializer(obj.product).data