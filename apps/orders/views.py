from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class OrderView(TemplateView):
    template_name = 'order.html'


class PlaceOrderView(TemplateView):
    template_name = 'place_order.html'


class PurchaseOrderView(TemplateView):
    template_name = 'purchase_order.html'

    def get_context_data(self, **kwargs):
        context = super(PurchaseOrderView, self).get_context_data(**kwargs)
        context['order_number'] = kwargs['order_number']
        context['mama'] = 123
        return context
