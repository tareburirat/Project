from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.products.models import Product, ProductImage
from apps.products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


@api_view(['post'])
def save_product(request):
    data = request.data

    images = data.pop('image_set')
    with transaction.atomic():
        name = data['name']
        price = int(data['price'])
        product_status = int(data['status'])
        freight_fee = int(data['freight_fee'])
        freight = int(data['freight'])
        seller_id = int(data['seller_id'])

        product = Product.objects.create(
            name=name,
            price=price,
            product_status=product_status,
            freight_fee=freight_fee,
            freight=freight,
            seller_id=seller_id
        )

        for image in images:
            ProductImage.objects.create(product=product, image=image)

    return Response(status=status.HTTP_200_OK, data={'message': "success!"})
