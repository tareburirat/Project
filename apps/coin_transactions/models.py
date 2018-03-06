from django.db import models

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
        account = self.account
        if self.transaction_type is self.deposit:
            account.coin += int(self.amount)
        elif self.transaction_type in [self.withdraw, self.usage]:
            account.coin -= int(self.amount)
        account.save()
        return super(CoinTransaction, self).save(*args, **kwargs)
