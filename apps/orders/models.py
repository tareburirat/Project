from django.db import models

# Create your models here.
from apps.accounts.models import Account
from apps.products.models import Product


class Order(models.Model):
    buyer = models.ForeignKey(Account)
    seller = models.ForeignKey(Account, related_name='sales', related_query_name='sales')
    product = models.ForeignKey(Product)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(auto_now=True)
