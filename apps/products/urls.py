from django.conf.urls import url

from apps.products.views import ProductView, SingleProductView, AddProductView

urlpatterns = [
    url(r'^$', ProductView.as_view()),
    url(r'^single/(?P<pk>\d+)', SingleProductView.as_view()),
    url(r'^create_product/', AddProductView.as_view()),

]

