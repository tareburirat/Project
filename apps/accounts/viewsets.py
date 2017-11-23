from rest_framework import viewsets

from apps.accounts.models import Account
from apps.accounts.serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
