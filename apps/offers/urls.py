from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.OfferView.as_view(), name='offers'),

]
