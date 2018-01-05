from django.views.generic import TemplateView


# Create your views here.
class ProductView(TemplateView):
    template_name = 'product.html'


class AddProductView(TemplateView):
    template_name = 'create_product.html'


class SingleProductView(TemplateView):
    template_name = 'single.html'

    def get_context_data(self, **kwargs):
        context = super(SingleProductView, self).get_context_data(**kwargs)

        context['product_id'] = kwargs.get('pk')
        return context

