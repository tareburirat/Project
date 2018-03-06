from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(verbose_name="First Name", max_length=100)
    last_name = models.CharField(verbose_name="Last Name", max_length=100)
    email = models.EmailField(verbose_name="Email", null=True, blank=True)
    display_name = models.CharField(verbose_name="Display Name", max_length=100, unique=True)
    phone = models.CharField(verbose_name="Telephone", max_length=50, null=True, blank=True)
    product_active_period = models.IntegerField(verbose_name="Expire Date", default=3)
    coin = models.IntegerField(verbose_name="Coin", default=0)

    def __str__(self):
        return self.display_name
