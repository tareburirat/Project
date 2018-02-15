from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class OrderView(TemplateView):
    template_name = 'order.html'


class PlaceOrderView(TemplateView):
    template_name = 'place_order.html'


class PurchaseOrderView(TemplateView):
    template_name = 'purchase_order.html'