from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class AddCoinsView(TemplateView):
    template_name = 'add_coins.html'