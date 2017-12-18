from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ProductView(TemplateView):
    template_name = 'product.html'

class AddProductView(TemplateView):
    template_name = 'create_product.html'


