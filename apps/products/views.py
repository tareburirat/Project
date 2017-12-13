from django.shortcuts import render
from django.views.generic import TemplateView
from apps.products.models import Product
# Create your views here.



class ProductView(TemplateView):
    template_name = 'product.html'


