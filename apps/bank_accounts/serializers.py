from rest_framework import serializers

from apps.bank_accounts.models import BankAccount


class BankAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankAccount
        exclude = ['security_number']
