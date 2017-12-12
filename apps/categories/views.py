from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class CategoryView(TemplateView):
    template_name = 'category.html'