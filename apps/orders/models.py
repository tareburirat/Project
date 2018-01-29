from django.db import models

# Create your models here.
from apps.accounts.models import Account
from apps.products.models import Product


class Order(models.Model):
    buyer = models.ForeignKey(Account)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        self.update_product_not_available()
        return super(Order, self).save(*args, **kwargs)

    def update_product_not_available(self):
        product_id_list = self.order_items.values_list('product_id', flat=True)
        Product.objects.filter(id__in=product_id_list).update(product_status=Product.sold)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product = models.ForeignKey(Product)
    seller = models.ForeignKey(Account, related_name='sales', related_query_name='sales')
