from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class AddressBuyerView(TemplateView):
    template_name = 'address_buyer.html'