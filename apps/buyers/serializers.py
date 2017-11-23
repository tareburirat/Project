from rest_framework import serializers

from apps.buyers.models import Buyer


class BuyerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Buyer
        exclude = []

