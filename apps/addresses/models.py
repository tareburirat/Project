from django.db import models

# Create your models here.
from apps.accounts.models import Account


class Address(models.Model):

    deliver = 0
    normal = 1


    address_detail_choices = [
        (deliver, "deliver"),
        (normal, "normal"),

    ]

    buyer = models.ForeignKey(Account)
    address_details = models.CharField(verbose_name="Address",max_length=200)
    address_choices = models.IntegerField(verbose_name="AddressChoices", choices=address_detail_choices, default=deliver)
    primary = models.BooleanField(verbose_name="PrimaryAddress",default=True)