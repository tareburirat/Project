from django.db import models

# Create your models here.
from apps.accounts.models import Account


class Address(models.Model):

    deliver = 0
    normal = 1

    address_detail_choices = [
        (deliver, "deliver"),
        (normal, "normal"),

    ]

    buyer = models.ForeignKey(Account)
    address_details = models.CharField(verbose_name="Address", max_length=200)
    address_choices = models.IntegerField(verbose_name="AddressChoices", choices=address_detail_choices, default=deliver)
    primary = models.BooleanField(verbose_name="PrimaryAddress", default=True)

    def save(self, *args, **kwargs):
        self.validate_primary_address()
        return super(Address, self).save(*args, **kwargs)

    def validate_primary_address(self):
        if self.primary is True:
            self.buyer.address_set.all().update(primary=False)

    def __str__(self):
        return "Address - {}(buyer)".format(self.buyer_id)

    def delete(self, *args, **kwargs):
        self.validate_primary_address_delete()
        return super(Address, self).delete(*args, **kwargs)

    def validate_primary_address_delete(self):
        if self.primary is True:
            try:
                last_address = self.buyer.address_set.exclude(id=self.id).order_by('id').last()
                last_address.primary = True
                last_address.save()
            except self.DoesNotExist:
                pass
            except AttributeError:
                pass






