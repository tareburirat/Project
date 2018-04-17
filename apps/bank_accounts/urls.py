from django.conf.urls import url

from apps.bank_accounts.views import BankAccountPickOrCreate

urlpatterns = [
    url(r'^pick_or_create/', BankAccountPickOrCreate.as_view()),
]
