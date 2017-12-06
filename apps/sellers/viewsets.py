from rest_framework import viewsets


from apps.sellers.models import Seller
from apps.sellers.serializers import SellerSerializer


class SellerViewSet(viewsets.ModelViewSet):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()