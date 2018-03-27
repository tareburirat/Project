from rest_framework import serializers

from apps.bank_accounts.models import BankAccount


class BankAccountSerializer(serializers.ModelSerializer):
    bank_name = serializers.SerializerMethodField()
    account_number_display = serializers.SerializerMethodField()

    class Meta:
        model = BankAccount
        exclude = ['security_number']

    @staticmethod
    def get_bank_name(obj):
        return obj.get_bank_display()

    @staticmethod
    def get_account_number_display(obj):
        return ("*" * (len(obj.account_number) - 4)) + obj.account_number[-4:]
