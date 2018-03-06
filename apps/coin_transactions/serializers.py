from rest_framework import serializers

from apps.coin_transactions.models import CoinTransaction
from apps.products.serializers import SimpleProductSerializer


class CoinTransactionSerializer(serializers.ModelSerializer):
    promoted_product_data = serializers.SerializerMethodField

    class Meta:
        model = CoinTransaction
        exclude = []

    @staticmethod
    def get_promoted_product_data(obj):
        return SimpleProductSerializer(obj.promoted_product).data
