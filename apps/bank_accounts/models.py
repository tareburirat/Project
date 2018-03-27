from django.db import models

from apps.accounts.models import Account


class BankAccount(models.Model):
    other = -1
    bbl = 0
    kbank = 1
    scb = 2
    ktb = 3
    tmb = 4
    krungsri = 5
    tanachart = 6
    uob = 7
    tisco = 8
    lhbank = 9
    cimb = 10
    gsb = 11
    bank_choices = [
        (other, "Others"),
        (bbl, "BBL"),
        (kbank, "Kbank"),
        (scb, "Scb"),
        (ktb, "Ktb"),
        (tmb, "Tmb"),
        (krungsri, "Krungsri"),
        (tanachart, "Tanachart"),
        (uob, "Uob"),
        (tisco, "Tisco"),
        (lhbank, "Lh"),
        (cimb, "Cimb"),
        (gsb, "Gsb")
    ]
    bank = models.IntegerField(default=other, choices=bank_choices)
    account_number = models.CharField(max_length=50, blank=True)
    security_number = models.CharField(max_length=10, blank=True)
    account_owner = models.ForeignKey(Account)

    promptpay_phone_number = models.CharField(max_length=20, blank=True)
    promptpay_citizen_id = models.CharField(max_length=20, blank=True)

    visa = 0
    mastercard = 1
    card_type_choices = [
        (visa, "Visa"),
        (mastercard, "Mastercard")
    ]
    card_type = models.IntegerField(default=visa, choices=card_type_choices)
    is_active = models.BooleanField(default=True, blank=True)
    is_primary = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.validate_primary()
        return super(BankAccount, self).save(*args, **kwargs)

    def validate_primary(self):
        if self.is_primary is True:
            self.account_owner.bankaccount_set.all().update(is_primary=False)
            self.is_primary = True
