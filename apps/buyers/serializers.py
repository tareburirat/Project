from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import transaction, IntegrityError
from rest_framework import serializers

from apps.accounts.models import Account
from apps.accounts.serializers import AccountSerializer
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
                print(validated_data)
                account_data = validated_data.pop('account')
                user = account_data.pop('user')
                user_obj = User.objects.create(**user)
                account = Account.objects.create(
                    user=user_obj,
                    **account_data
                )

                buyer = Buyer.objects.create(
                    account=account,
                    **validated_data
                )
        except IntegrityError:
            raise ValidationError("Custom Error, something went wrong.")
        return buyer
