from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class OfferView(TemplateView):
    template_name = 'offer.html'