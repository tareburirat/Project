from django.conf.urls import url

from apps.accounts.views import EditProfileView
from apps.my_profile.views import ProfileView
from apps.products.views import MyProductView

urlpatterns = [
    url(r'edit', EditProfileView.as_view()),
    url(r'^profile/', ProfileView.as_view()),
    url(r'^my_product/', MyProductView.as_view()),
]

