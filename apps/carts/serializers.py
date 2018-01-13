from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers

from apps.carts.models import Cart


class CartSerializer(serializers.ModelSerializer):

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
