from django.db import models
from django.utils import timezone

from apps.accounts.models import Account
from apps.products.models import Product


class CoinTransaction(models.Model):
    deposit = 0
    withdraw = 1
    usage = 2
    transaction_choices = [
        (deposit, "Deposit"),
        (withdraw, "Withdraw"),
        (usage, "Usage")
    ]

    account = models.ForeignKey(Account, verbose_name="Transaction Owner")
    transaction_type = models.IntegerField(verbose_name="Transaction Type", choices=transaction_choices)
    amount = models.IntegerField(verbose_name="Amount", default=0)
    promoted_product = models.ForeignKey(Product, null=True, blank=True)

    def __str__(self):
        return "{} {} {} (product_id: {})".format(self.account.display_name, self.get_transaction_type_display(),
                                                  self.amount, self.promoted_product_id)

    def save(self, *args, **kwargs):
        self.update_account_accordingly()

        return super(CoinTransaction, self).save(*args, **kwargs)

    def update_account_accordingly(self):
        account = self.account
        if self.transaction_type is self.deposit:
            account.coin += int(self.amount)
            self.promoted_product = None
        elif self.transaction_type is self.withdraw:
            account.coin -= int(self.amount)
            self.promoted_product = None
        elif self.transaction_type is self.usage:
            account.coin -= int(self.amount)
            self.append_promotion_time()
        account.save()

    def append_promotion_time(self):
        product = self.promoted_product
        product.exp_date_promotion = timezone.now() + timezone.timedelta(hours=12)
        product.save()

