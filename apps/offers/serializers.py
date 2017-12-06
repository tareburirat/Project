from rest_framework import serializers

from apps.offers.models import Offer


class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        exclude = []
