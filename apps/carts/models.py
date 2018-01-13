from django.db import models

from apps.accounts.models import Account
from apps.products.models import Product


class Cart(models.Model):

    owner = models.ForeignKey(Account)
    product = models.ForeignKey(Product)
    in_cart = models.BooleanField(verbose_name="Status", default=True)

