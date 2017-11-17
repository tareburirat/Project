from django.db import models

# Create your models here.
from apps.categories.models import Category
from apps.products.models import Product


class CategoryProduct(models.Model):
    category = models.ForeignKey(Category)
    product = models.ForeignKey(Product)