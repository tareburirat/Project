from django.views.generic import TemplateView


class ProductView(TemplateView):
    template_name = 'product.html'


class CreateProductView(TemplateView):
    template_name = 'create_product.html'


