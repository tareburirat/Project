from django.db import models

# Create your models here.
from apps.buyers.models import Buyer
from apps.products.models import Product


class Offer (models.Model):

    decline = -1
    pending = 0
    accept = 1
    rejected = 2
    revoked = 3

    status_choices = [
        (decline, "Decline"),
        (pending, "Pending"),
        (accept, "Accept"),
        (rejected, "Rejected"),
        (revoked, "Revoked"),
    ]

    offer_price = models.DecimalField(verbose_name="Offer Price", max_digits=8, decimal_places=2, default=0)
    status = models.IntegerField(verbose_name="Status", choices=status_choices, default=pending)
    buyer = models.ForeignKey(Buyer)
    product = models.ForeignKey(Product)