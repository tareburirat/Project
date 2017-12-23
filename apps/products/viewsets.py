from django.core.exceptions import ValidationError
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.products.models import Product, ProductImage
from apps.products.serializers import ProductSerializer
from apps.properties.models import Property


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

@csrf_exempt
@api_view(['post'])
def save_product(request):
    data = request.data

    images = data.getlist('images[]')
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


@api_view(['post'])
def get_product_properties(request):
    try:
        data = request.data
        category_id = data['category_id']
        properties = Property.objects.filter(category_id=category_id).values_list('text', flat=True)
        if len(properties) > 1:
            raise ValidationError
    except KeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Bad request data!!!'})
    except ValidationError:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'No properties found!!!'})
    finally:
        return Response(status=status.HTTP_200_OK, data={'properties': properties})
