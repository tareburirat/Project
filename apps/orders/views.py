from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class OrderView(TemplateView):
    template_name = 'order.html'