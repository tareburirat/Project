from django.db import models

# Create your models here.
from apps.buyers.models import Buyer
from apps.products.models import Product
from apps.sellers.models import Seller


class Order(models.Model):
    buyer = models.ForeignKey(Buyer)
    seller = models.ForeignKey(Seller)
    product = models.ForeignKey(Product)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(auto_now=True)