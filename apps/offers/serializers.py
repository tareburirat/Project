from rest_framework import serializers

from apps.offers.models import Offer


class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        exclude = []

    def create(self, validated_data):
        if validated_data['buyer'] == validated_data['product'].seller_id:
            serializers.ValidationError('Cannot Buy Own Product')
        return super(OfferSerializer, self).create(validated_data)
