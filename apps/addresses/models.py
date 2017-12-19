from django.db import models

# Create your models here.
from apps.accounts.models import Account


class Address(models.Model):
    buyer = models.ForeignKey(Account)
    address_details = models.CharField(verbose_name="Address",max_length=200)
