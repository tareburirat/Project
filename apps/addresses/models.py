from django.db import models

# Create your models here.
from apps.buyers.models import Buyer


class Address(models.Model):
    buyer = models.ForeignKey(Buyer)
    address_details = models.CharField(verbose_name="Address",max_length=200)
