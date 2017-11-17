from django.db import models

# Create your models here.
from apps.sellers.models import Seller


class Product (models.Model):
    banned = -2
    expired = -1
    draft = 0
    sale = 1
    booked = 2
    sold = 3

    status_choices = [
        (banned, "Banned"),
        (expired, "Expired"),
        (draft, "Draft"),
        (sale, "Sale"),
        (booked, "Booked"),
        (sold, "Sold"),
    ]

    reg = 0
    ems = 1
    kerry = 2

    freight_detail_choices =[
        (reg, "Register"),
        (ems, "EMS"),
        (kerry, "Kerry Express"),
    ]

    status = models.IntegerField(verbose_name="Status", choices=status_choices, default=draft)
    date_of_sale = models.DateField(verbose_name="Date of Sale", auto_now=True)
    seller = models.ForeignKey(Seller)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    name = models.CharField(verbose_name="Name", max_length=200)
    freight = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    freight_detail_choices = models.IntegerField(verbose_name="Freight Detail", choices=freight_detail_choices, default=reg)

    def __str__(self):
        return self.name




