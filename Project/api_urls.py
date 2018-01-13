from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.accounts.viewsets import AccountViewSet, create_account, password_change
from apps.addresses.viewsets import AddressViewSet
from apps.carts.viewsets import CartViewSet
from apps.categories.viewsets import CategoryViewSet
from apps.category_product.viewset import CategoryProductViewSet
from apps.offers.viewsets import OfferViewSet
from apps.orders.viewsets import OrderViewSet
from apps.products import viewsets as product_viewsets
from apps.properties.viewsets import PropertyViewSet
from apps.ratings.viewsets import RatingViewSet
from apps.transactions.viewsets import TransactionViewSet
from apps.values.viewsets import ValueViewSet

router = DefaultRouter()
router.register('accounts', AccountViewSet, base_name='account')
router.register('addresses', AddressViewSet, base_name='address')
router.register('carts', CartViewSet, base_name='cart')
router.register('categories', CategoryViewSet, base_name='category')
router.register('offers', OfferViewSet, base_name='offer')
router.register('orders', OrderViewSet, base_name='order')
router.register('products', product_viewsets.ProductViewSet, base_name='product')
router.register('properties', PropertyViewSet, base_name='property')
router.register('ratings', RatingViewSet, base_name='rating')
router.register('transactions', TransactionViewSet, base_name='transaction')
router.register('values', ValueViewSet, base_name='value')
router.register('categoryProducts', CategoryProductViewSet, base_name='categoryProduct')


urlpatterns = [
    # account functions
    url(r'^create_account/', create_account),
    url(r'^password_change/', password_change),

    # product functions
    url(r'^save_products/', product_viewsets.save_product),
    url(r'^get_product_properties/', product_viewsets.get_product_properties),
]
urlpatterns += router.urls
