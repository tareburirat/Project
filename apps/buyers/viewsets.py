from rest_framework import viewsets

from apps.buyers.models import Buyer
from apps.buyers.serializers import BuyerSerializer


class BuyerViewSet(viewsets.ModelViewSet):
    serializer_class = BuyerSerializer
    queryset = Buyer.objects.all()