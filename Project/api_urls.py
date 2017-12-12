from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from apps.accounts.viewsets import AccountViewSet
from apps.addresses.viewsets import AddressViewSet
from apps.buyers.viewsets import BuyerViewSet
from apps.categories.viewsets import CategoryViewSet
from apps.offers.viewsets import OfferViewSet
from apps.orders.viewsets import OrderViewSet
from apps.products.viewsets import ProductViewSet, save_product
from apps.properties.viewsets import PropertyViewSet
from apps.ratings.viewsets import RatingViewSet
from apps.sellers.viewsets import SellerViewSet
from apps.transactions.viewsets import TransactionViewSet
from apps.values.viewsets import ValueViewSet

router = DefaultRouter()
router.register('accounts', AccountViewSet, base_name='account')
router.register('addresses', AddressViewSet, base_name='address')
router.register('buyers', BuyerViewSet, base_name='buyer')
router.register('categories', CategoryViewSet, base_name='category')
router.register('offers', OfferViewSet, base_name='offer')
router.register('orders', OrderViewSet, base_name='order')
router.register('products', ProductViewSet, base_name='product')
router.register('properties', PropertyViewSet, base_name='property')
router.register('ratings', RatingViewSet, base_name='rating')
router.register('seller', SellerViewSet, base_name='seller')
router.register('transactions', TransactionViewSet, base_name='transaction')
router.register('values', ValueViewSet, base_name='value')


urlpatterns = [
    url(r'^save_products/', save_product),
]
urlpatterns += router.urls
