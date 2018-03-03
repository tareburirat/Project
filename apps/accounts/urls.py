from django.conf.urls import url

from apps.accounts.views import EditProfileView, ChangePassWordView
from apps.addresses.views import AddressBuyerView
from apps.my_profile.views import ProfileView, PurchaseHistoryView, SalesHistoryView
from apps.products.views import MyProductView

urlpatterns = [
    url(r'edit', EditProfileView.as_view()),
    url(r'^profile/', ProfileView.as_view()),
    url(r'^my_product/', MyProductView.as_view()),
    url(r'^change_password/', ChangePassWordView.as_view()),
    url(r'^purchase_history/', PurchaseHistoryView.as_view()),
    url(r'^sales_history/', SalesHistoryView.as_view()),
    url(r'^address_buyer/', AddressBuyerView.as_view()),

]

