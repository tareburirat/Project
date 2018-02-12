from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe

from apps.accounts.models import Account


class Product(models.Model):
    banned = -2
    expired = -1
    draft = 0
    sale = 1
    booked = 2
    sold = 3

    status_choices = [
        (banned, "Banned"),
        (expired, "Expired"),
        (draft, "Draft"),
        (sale, "Sale"),
        (booked, "Booked"),
        (sold, "Sold"),
    ]

    other = -1
    reg = 0
    ems = 1
    kerry = 2

    freight_detail_choices =[
        (reg, "Register"),
        (ems, "EMS"),
        (kerry, "Kerry Express"),

    ]

    new = 0
    used = 1

    product_quality_choice = [
        (new, "New"),
        (used, "Used"),
    ]

    product_status = models.IntegerField(verbose_name="Status", choices=status_choices, default=sale)
    date_of_sale = models.DateTimeField(verbose_name="Date of Sale", auto_now=True)
    seller = models.ForeignKey(Account)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    name = models.CharField(verbose_name="Name", max_length=200)
    freight_fee = models.DecimalField(verbose_name="Freight Fee", max_digits=8, decimal_places=2, default=0)
    freight = models.IntegerField(verbose_name="Freight", choices=freight_detail_choices, default=reg)
    product_quality = models.IntegerField(verbose_name="Quality", choices=product_quality_choice, default=used)
    detail = models.CharField(verbose_name="Details", max_length=255, blank=True)

    def __str__(self):
        return self.name

    @property
    def properties(self):
        values = self.value_set.all()
        properties_and_values = dict([(x.properties_string, x.value_product) for x in values])
        return properties_and_values


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="images")
    image = models.ImageField(upload_to="product_images")
    sequence = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.product, self.sequence)

    def image_tag(self):
        return mark_safe('<img src="/images/{}" width="200" height="150" />'.format(self.image.name))

    image_tag.short_description = 'Image'


class ProductSummary(Product):

    class Meta:
        proxy = True
        verbose_name = 'Product Summary'
        verbose_name_plural = 'Products Summary'


