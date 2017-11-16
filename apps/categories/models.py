from django.db import models

# Create your models here.


class Category(models.Model):
    normal = 0
    promotion = 1
    group = 2
    tag = 3
    type_choices = [
        (normal, "Normal"),
        (promotion, "Promotion"),
        (group, "Group"),
        (tag, "Tags"),
    ]

    name = models.CharField(verbose_name="Category Name", max_length=500)
    category_type = models.IntegerField(verbose_name="Type", choices=type_choices, default=normal)
