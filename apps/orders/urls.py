from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^place_order', views.PlaceOrderView.as_view(), name='place_order'),
    url(r'^purchase_order', views.PurchaseOrderView.as_view(), name='purchase_order'),
]
