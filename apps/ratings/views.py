from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class RatingView(TemplateView):
    template_name = 'rating.html'