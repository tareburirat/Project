from django.db import models

# Create your models here.
from apps.products.models import Product


class Value(models.Model):
    product = models.ForeignKey(Product)
    properties_string = models.CharField(max_length=100)
    value_product = models.CharField(max_length=100)
