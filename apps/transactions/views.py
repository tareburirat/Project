from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class TransactionView(TemplateView):
    template_name = 'transaction.html'