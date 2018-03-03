import copy
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers

from apps.carts.models import Cart
from apps.offers.models import Offer
from apps.products.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    product_data = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        exclude = []
        extra_kwargs = {
            'in_cart': {
                'initial': True
            }
        }

    def create(self, validated_data):
        context = copy.copy(validated_data)

        offers = Offer.objects.filter(product_id=context['product'].id, offer_status=Offer.accept)
        if offers.exists():
            context['sale_price'] = offers.first().offer_price
        else:
            context['sale_price'] = context['product'].price

        return super(CartSerializer, self).create(context)

    def get_product_data(self, obj):
        return ProductSerializer(obj.product).data
