from rest_framework import viewsets

from apps.carts.models import Cart
from apps.carts.serializers import CartSerializer


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
