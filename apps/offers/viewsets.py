from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.offers.models import Offer
from apps.offers.serializers import OfferSerializer
from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class OfferViewSet(viewsets.ModelViewSet):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()


@api_view(['GET'])
def get_highest_offer_for_all_products(request):
    highest_price_product_list = []
    added_product_ids = set()
    try:
        seller_id = request.data['seller_id']
        if seller_id is None:
            raise KeyError()
        offers = Offer.objects.filter(offer_status=Offer.pending, product__seller_id=seller_id).order_by('-offer_price', 'id')

        for offer in offers:
            if offer.product_id not in added_product_ids:
                added_product_ids.add(offer.product_id)
                highest_price_product_list.append(offer)

        return Response(status=status.HTTP_200_OK, data={'products': ProductSerializer(highest_price_product_list).data})

    except (KeyError, ValueError):
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'seller_id is invalid or missing jaa'})


@api_view(['POST'])
def reject_or_accept_product_offer(request):
    data = request.data
    try:
        product_id = data['product_id']
        offer_id = data['offer_id']
        offer_accepted= data['offer_accepted']

        if offer_accepted is True:
            # validate product
            if Product.objects.filter(id=product_id, status=Product.sale).exists() is not True:
                raise Product.DoesNotExist()

            offer = Offer.objects.get(id=offer_id)
            offer.offer_status = Offer.accept
            offer.save()

        Offer.objects.filter(product_id=product_id, offer_status=Offer.pending).update(offer_status=Offer.rejected)

    except (KeyError, Product.DoesNotExist):
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'request is invalid jaa'})
