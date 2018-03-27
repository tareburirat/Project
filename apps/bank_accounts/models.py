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
