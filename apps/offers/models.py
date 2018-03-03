from django.db import models

# Create your models here.
from apps.accounts.models import Account
from apps.carts.models import Cart
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

    offer_price = models.DecimalField(verbose_name="Price", max_digits=8, decimal_places=2, default=0)
    offer_status = models.IntegerField(verbose_name="Status", choices=status_choices, default=pending)
    buyer = models.ForeignKey(Account)
    product = models.ForeignKey(Product)

    class Meta:
        unique_together = ['buyer', 'product']

    def save(self, *args, **kwargs):

        if self.offer_status is self.accept:
            self.update_buyers_cart()

        return super(Offer, self).save(*args, **kwargs)

    def update_buyers_cart(self):
        Cart.objects.create(
            owner_id=self.buyer_id,
            product_id=self.product_id,
            sale_price=self.offer_price
        )
