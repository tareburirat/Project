from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class RegisterBuyerView(TemplateView):
    template_name = 'register_buyer.html'