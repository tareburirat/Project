from django.db import models

# Create your models here.
from apps.accounts.models import Account
from apps.orders.models import OrderItem


class Rating(models.Model):
    buyer = models.ForeignKey(Account, related_name='ratings', related_query_name='ratings')
    seller = models.ForeignKey(Account, related_name='shop_ratings', related_query_name='shop_ratings')
    order_item = models.ForeignKey(OrderItem, related_name='order_items', related_query_name='order_items')
    rating = models.PositiveSmallIntegerField(verbose_name="Rating", default=0)

    def __str__(self):
        return str(self.rating)