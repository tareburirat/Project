from rest_framework import viewsets

from apps.coin_transactions.models import CoinTransaction
from apps.coin_transactions.serializers import CoinTransactionSerializer


class CoinTransactionViewSet(viewsets.ModelViewSet):
    serializer_class = CoinTransactionSerializer
    queryset = CoinTransaction.objects.all()
