from django.db import models

from apps.accounts.models import Account
from apps.products.models import Product


class Cart(models.Model):

    owner = models.ForeignKey(Account)
    product = models.ForeignKey(Product)
    sale_price = models.IntegerField(default=0)
    in_cart = models.BooleanField(verbose_name="Status", default=True)

    def __str__(self):
        return "Id:{}, product id: {}".format(self.id, self.product_id)
