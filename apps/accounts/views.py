from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class AccountRegisterView(TemplateView):
    template_name = 'account_register.html'