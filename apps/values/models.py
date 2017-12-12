from django.db import models

# Create your models here.
from apps.products.models import Product
from apps.properties.models import Property


class Value(models.Model):
    product = models.ForeignKey(Product)
    properties = models.ForeignKey(Property)
    properties_string = models.CharField(verbose_name="Batch Code", max_length=100, blank=True)
    value_product = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.properties_string = self.properties.text
        return super(Value, self).save(*args, **kwargs)
