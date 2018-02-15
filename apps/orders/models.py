from django.db import models

# Create your models here.
from apps.accounts.models import Account
from apps.carts.models import Cart
from apps.offers.models import Offer
from apps.products.models import Product


class Order(models.Model):
    buyer = models.ForeignKey(Account)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        self.update_product_not_available()
        return super(Order, self).save(*args, **kwargs)

    def update_product_not_available(self):
        product_id_list = self.buyer.cart_set.values_list('product_id', flat=True)
        Product.objects.filter(id__in=product_id_list).update(product_status=Product.sold)
        Cart.objects.filter(product_id__in=product_id_list).update(in_cart=False)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product = models.ForeignKey(Product)
    seller = models.ForeignKey(Account, related_name='sales', related_query_name='sales')

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        self.check_offer()  # if the offer was accepted
        return super(OrderItem, self).save(*args, **kwargs)

    def check_offer(self):
        offers = Offer.objects.filter(product_id=self.product_id, offer_status=Offer.accept)
        if offers.exists():
            self.price = offers.first().offer_price
