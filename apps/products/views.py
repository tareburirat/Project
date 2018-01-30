from django.views.generic import TemplateView

from apps.categories.models import Category
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


class ProductSearchView(TemplateView):
    template_name = 'search_product.html'

    def get_context_data(self, **kwargs):
        context = super(ProductSearchView, self).get_context_data(**kwargs)
        data = self.request.GET
        context['query_string'] = dict(data)
        product_name = data.get("product_name", "")
        try:
            cat_id = data.get("category", "")
            # cat_name = Category.objects.get(id=cat_id).name
        except Category.DoesNotExist:
            cat_id = ""  # default value when nothing is found
        context['bread_crumb_text'] = product_name or cat_id
        return context
