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

    status = models.IntegerField(verbose_name="Status", choices=status_choices, default=draft)
    date_of_sale = models.DateField(verbose_name="Date of Sale",auto_now=True)
    seller = models.ForeignKey(Seller)
