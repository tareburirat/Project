from rest_framework import viewsets

from apps.bank_accounts.models import BankAccount
from apps.bank_accounts.serializers import BankAccountSerializer


class BankAccountViewSet(viewsets.ModelViewSet):
    serializer_class = BankAccountSerializer
    queryset = BankAccount.objects.filter(is_active=True)

