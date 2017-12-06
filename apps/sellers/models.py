from django.db import models

# Create your models here.
from apps.accounts.models import Account


class Seller (models.Model):
    phone_number = models.CharField(verbose_name="Tel", max_length=20)
    expire_date = models.IntegerField(verbose_name="Date Expiredate", default=0)
    account = models.OneToOneField(Account)

    def __str__(self):
        return "Seller: {}".format(self.account.display_name)