from django.core.exceptions import ValidationError
from django.db import transaction, IntegrityError
from rest_framework import serializers

from apps.accounts.models import Account
from apps.accounts.serializers import AccountSerializer
from apps.addresses.serializers import AddressSerializer
from apps.buyers.models import Buyer



class BuyerSerializer(serializers.ModelSerializer):
    account = AccountSerializer(many=False)

    class Meta:
        model = Buyer
        fields = [
            'id',
            'phone_number',
            'account',
        ]

    def create(self, validated_data):
        try:
            with transaction.atomic():
                account_data = validated_data.pop('account')
                account = Account.objects.create(**account_data)

                print(validated_data)
                buyer = Buyer.objects.create(
                    account=account,
                    **validated_data
                )
        except IntegrityError:
            raise ValidationError("Custom Error, something went wrong.")
        return buyer
