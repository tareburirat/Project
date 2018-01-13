from django.core.exceptions import ValidationError
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.category_product.models import CategoryProduct
from apps.products.models import Product, ProductImage
from apps.products.serializers import ProductSerializer
from apps.properties.models import Property
from apps.values.models import Value


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['seller_id']

@csrf_exempt
@api_view(['post'])
def save_product(request):
    data = request.data

    images = data.getlist('images[]')
    with transaction.atomic():
        name = data['name']
        price = int(data['price'])
        freight_fee = int(data['freight_fee'])
        freight = int(data['freight'])
        seller_id = int(data['seller_id'])
        cat_id = data['category_id']

        product = Product.objects.create(
            name=name,
            price=price,
            freight_fee=freight_fee,
            freight=freight,
            seller_id=seller_id
        )

        for image in images:
            ProductImage.objects.create(product=product, image=image)

        CategoryProduct.objects.create(category_id=cat_id, product_id=product.id)

        for p_id, p_value in zip(request.data.getlist('propertyId[]'), request.data.getlist('propertyValue[]')):
            Value.objects.create(properties_id=p_id, value_product=p_value, product=product)

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
