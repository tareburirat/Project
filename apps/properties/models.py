from django.db import models

# Create your models here.
from apps.categories.models import Category


class Property(models.Model):
    category = models.ForeignKey(Category)
    text = models.CharField(verbose_name="Detail", max_length=255)

    def __str__(self):
        return self.text
