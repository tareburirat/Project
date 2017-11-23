from rest_framework import viewsets

from apps.offers.models import Offer
from apps.offers.serializers import OfferSerializer


class OfferViewSet(viewsets.ModelViewSet):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()
