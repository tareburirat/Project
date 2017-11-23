from rest_framework import viewsets

from apps.properties.models import Property
from apps.properties.serializers import PropertySerializer


class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()