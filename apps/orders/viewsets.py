from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apps.orders.models import Order, OrderItem
from apps.orders.serializers import OrderSerializer, OrderItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['order_number', 'id']


class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all().order_by('-id')
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['order_id', 'id', 'seller_id', 'order__buyer_id', 'order_status']
