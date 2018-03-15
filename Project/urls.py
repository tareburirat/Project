"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from apps.carts.views import CartView
from apps.login.views import log_in_user, LoginView, log_out
from apps.addresses.views import AddressBuyerView
from apps.categories.views import CategoryView
from apps.transactions.views import TransactionView
from apps.category_product.views import CategoryProductView
from apps.offers.views import OfferView
from apps.orders.views import OrderView
from apps.products.views import ProductView, AddProductView, SingleProductView, ProductSearchView
from apps.properties.views import PropertyView
from apps.ratings.views import RatingView
from apps.accounts.views import SignUpView, EditProfileView
from apps.values.views import ValueView
from apps.home.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('Project.api_urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^signup/', SignUpView.as_view(), name='signup'),
    url(r'^login/', LoginView.as_view()),
    url(r'^logout/', log_out, name='logout'),
    url(r'^authenticate_user/', log_in_user),
    url(r'^product_search/', ProductSearchView.as_view()),

    url(r'^product/', include('apps.products.urls')),
    url(r'^order/', include('apps.orders.urls')),
    url(r'^account/', include('apps.accounts.urls')),
    url(r'^cart/', include('apps.carts.urls')),
    url(r'^approve_offer/', include('apps.offers.urls')),
    url(r'^dashboard/', include('apps.admin_dashboard.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


