from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.accounts.viewsets import AccountViewSet, create_account, password_change, check_username, check_displayname
from apps.addresses.viewsets import AddressViewSet
from apps.carts.viewsets import CartViewSet
from apps.categories.viewsets import CategoryViewSet
from apps.category_product.viewset import CategoryProductViewSet
from apps.coin_transactions.viewsets import CoinTransactionViewSet
from apps.offers.viewsets import OfferViewSet, get_highest_offer_for_all_products, reject_or_accept_product_offer
from apps.orders.viewsets import OrderViewSet, OrderItemViewSet
from apps.products import viewsets as product_viewsets
from apps.properties.viewsets import PropertyViewSet
from apps.ratings.viewsets import RatingViewSet
from apps.transactions.viewsets import TransactionViewSet
from apps.values.viewsets import ValueViewSet

router = DefaultRouter()
router.register('accounts', AccountViewSet, base_name='account')
router.register('addresses', AddressViewSet, base_name='address')
router.register('categories', CategoryViewSet, base_name='category')
router.register('category_products', CategoryProductViewSet, base_name='category_product')
router.register('coin_transactions', CoinTransactionViewSet, base_name='coin_transaction')
router.register('carts', CartViewSet, base_name='cart')
router.register('offers', OfferViewSet, base_name='offer')
router.register('orders', OrderViewSet, base_name='order')
router.register('order_items', OrderItemViewSet, base_name='order_item')
router.register('products', product_viewsets.ProductViewSet, base_name='product')
router.register('properties', PropertyViewSet, base_name='property')
router.register('ratings', RatingViewSet, base_name='rating')
router.register('transactions', TransactionViewSet, base_name='transaction')
router.register('values', ValueViewSet, base_name='value')


urlpatterns = [
    # account functions
    url(r'^create_account/', create_account),
    url(r'^password_change/', password_change),
    url(r'^check_username/', check_username),
    url(r'^check_displayname/', check_displayname),

    # offer functions
    url(r'high_offers/', get_highest_offer_for_all_products),
    url(r'update_offers/', reject_or_accept_product_offer),

    # product functions
    url(r'^save_products/', product_viewsets.save_product),
    url(r'^get_product_properties/', product_viewsets.get_product_properties),
]
urlpatterns += router.urls
