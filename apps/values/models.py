from django.db import models

# Create your models here.
from apps.products.models import Product
from apps.properties.models import Property


class Value(models.Model):
    product = models.ForeignKey(Product)
    properties = models.ForeignKey(Property)
    properties_string = models.CharField(verbose_name="Batch Code", max_length=100)
    value_product = models.CharField(max_length=100)
