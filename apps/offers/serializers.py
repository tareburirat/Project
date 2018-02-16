from rest_framework import serializers

from apps.offers.models import Offer
from apps.products.serializers import ProductSerializer


class OfferSerializer(serializers.ModelSerializer):

    product_data = serializers.SerializerMethodField()

    class Meta:
        model = Offer
        exclude = []

    def create(self, validated_data):
        if validated_data['buyer'] == validated_data['product'].seller_id:
            serializers.ValidationError('Cannot Buy Own Product')
        return super(OfferSerializer, self).create(validated_data)

    def get_product_data(self, obj):
        return ProductSerializer(obj.product).data
