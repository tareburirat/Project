from django.views.generic import TemplateView
from .models import Product


# Create your views here.
class ProductView(TemplateView):
    template_name = 'product.html'


class AddProductView(TemplateView):
    template_name = 'create_product.html'

class MyProductView(TemplateView):
    template_name = 'my_product.html'


class SingleProductView(TemplateView):
    template_name = 'single.html'

    def get_context_data(self, **kwargs):
        context = super(SingleProductView, self).get_context_data(**kwargs)
        pk = kwargs.get('pk')

        context['product_id'] = pk
        context['product'] = Product.objects.get(id=pk)
        return context