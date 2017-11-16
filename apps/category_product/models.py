from django.db import models

# Create your models here.
from apps.categories.models import Category


class CategoryProduct(models.Model):
    category = models.ForeignKey(Category)