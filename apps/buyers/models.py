from django.db import models

# Create your models here.
from apps.accounts.models import Account


class Buyer(models.Model):
    account = models.OneToOneField(Account)
    phone_number = models.CharField(verbose_name="Phone Number", max_length=20)

    def __str__(self):
        return "Buyer: {}".format(self.account.display_name)

