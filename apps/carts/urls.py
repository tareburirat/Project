from django.conf.urls import url

from apps.carts.views import CartView

urlpatterns = [
    url(r'^$', CartView.as_view()),

]

