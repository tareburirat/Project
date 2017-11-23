from rest_framework import viewsets

from apps.values.models import Value
from apps.values.serailizers import ValueSerializer


class ValueViewSet(viewsets.ViewSet):

    serializer_class = ValueSerializer
    queryset = Value.objects.all()