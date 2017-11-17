from django.db import models

# Create your models here.
from apps.buyers.models import Buyer
from apps.products.models import Product


class Offer (models.Model):

    decline = -1
    pending = 0
    accept = 1

    status_choices = [
        (decline, "Decline"),
        (pending, "Pending"),
        (accept, "Accept"),

    ]

    offer_price = models.DecimalField(verbose_name="Offer Price",max_digits=8,decimal_places=2,)
    status = models.IntegerField(verbose_name="Status", choices=status_choices,default=pending)
    buyer = models.ForeignKey(Buyer)
    product = models.ForeignKey(Product)