import datetime
import random

from django.db import models

# Create your models here.
from apps.accounts.models import Account
from apps.carts.models import Cart
from apps.offers.models import Offer
from apps.products.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=30, blank=True)
    buyer = models.ForeignKey(Account)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(auto_now=True)
    order_address = models.CharField(max_length=200, blank=True)
    payment_slip = models.ImageField(upload_to="payment_slips", null=True, blank=True)

    def save(self, *args, **kwargs):
        self.update_product_not_available()
        self.gen_order_number()
        return super(Order, self).save(*args, **kwargs)

    def update_product_not_available(self):
        product_id_list = self.buyer.cart_set.values_list('product_id', flat=True)
        Product.objects.filter(id__in=product_id_list).update(product_status=Product.sold)
        Cart.objects.filter(product_id__in=product_id_list).update(in_cart=False)

    def gen_order_number(self):
        order_number = ""
        random_number = random.randint(0, 999)
        date_string = datetime.datetime.now().strftime('%d%m%Y')
        order_number += date_string + str(0).zfill(6) + str(random_number).zfill(3)
        self.order_number = order_number


class OrderItem(models.Model):
    draft = 0
    receive = 1
    success = 2

    status_choices = [
        (draft, "Draft"),
        (receive, "Receive"),
        (success, "Success"),
    ]

    order = models.ForeignKey(Order, related_name='order_items')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product = models.ForeignKey(Product)
    seller = models.ForeignKey(Account, related_name='sales', related_query_name='sales')
    order_status = models.IntegerField(verbose_name="Status", choices=status_choices, default=draft)
    order_track = models.CharField(verbose_name="Tracking", max_length=13, default="-รอการอัพเดท-")

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        self.check_offer()  # if the offer was accepted
        return super(OrderItem, self).save(*args, **kwargs)

    def check_offer(self):
        offers = Offer.objects.filter(product_id=self.product_id, offer_status=Offer.accept)
        if offers.exists():
            self.price = offers.first().offer_price