from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class CategoryProductView(TemplateView):
    template_name = 'category_product.html'