from rest_framework import viewsets

from apps.Transactions.models import Transaction
from apps.Transactions.serializers import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
