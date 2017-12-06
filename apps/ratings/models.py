from django.db import models

# Create your models here.
from apps.buyers.models import Buyer
from apps.sellers.models import Seller


class Rating(models.Model):
    buyer = models.ForeignKey(Buyer)
    seller = models.ForeignKey(Seller)
    rating = models.IntegerField(verbose_name="Rating", default=0)