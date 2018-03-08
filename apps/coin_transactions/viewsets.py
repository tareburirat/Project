from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apps.coin_transactions.models import CoinTransaction
from apps.coin_transactions.serializers import CoinTransactionSerializer


class CoinTransactionViewSet(viewsets.ModelViewSet):
    serializer_class = CoinTransactionSerializer
    queryset = CoinTransaction.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['account', 'id']
