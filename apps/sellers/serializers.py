from rest_framework import serializers

from apps.sellers.models import Seller


class SellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seller
        exclude = []