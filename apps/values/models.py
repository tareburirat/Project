from django.db import models

# Create your models here.
from apps.products.models import Product
from apps.properties.models import Property


class Value(models.Model):
    properties = models.ForeignKey(Property)
    product = models.ForeignKey(Product)
    properties_string = models.CharField(max_length=100)
    value_product = models.CharField(max_length=100)
