from rest_framework import viewsets

from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()