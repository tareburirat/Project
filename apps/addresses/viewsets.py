from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apps.addresses.models import Address
from apps.addresses.serializers import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all().order_by('id')
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['buyer_id']
