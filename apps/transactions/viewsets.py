from rest_framework import viewsets

from apps.transactions.models import Transaction
from apps.transactions.serializers import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
