from django.views.generic import TemplateView

# Create your views here.


class CartView(TemplateView):
    template_name = 'cart.html'