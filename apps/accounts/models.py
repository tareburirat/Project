from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    first_name = models.CharField(verbose_name="First Name", max_length=100)
    last_name = models.CharField(verbose_name="Last Name", max_length=100)
    email = models.EmailField(verbose_name="Email", null=True, blank=True)
    display_name = models.CharField(verbose_name="Display Name", max_length=100, unique=True)
