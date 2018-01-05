from django.db import models

# Create your models here.
from apps.accounts.models import Account


class Rating(models.Model):
    buyer = models.ForeignKey(Account, related_name='ratings', related_query_name='ratings')
    seller = models.ForeignKey(Account, related_name='shop_ratings', related_query_name='shop_ratings')
    rating = models.PositiveSmallIntegerField(verbose_name="Rating", default=0)
