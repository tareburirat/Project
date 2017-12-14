from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from rest_framework import serializers

from apps.accounts.models import Account
from apps.accounts.serializers import AccountSerializer
from apps.addresses.models import Address
from apps.addresses.serializers import AddressSerializer
from apps.sellers.models import Seller


class SellerSerializer(serializers.ModelSerializer):
    account = AccountSerializer(many=False)

    address = serializers.CharField(read_only=True)
    country = serializers.CharField(label='Country', write_only=True)
    city = serializers.CharField(label='City', write_only=True)
    zip_code = serializers.CharField(label='Zip Code', write_only=True)
    detail_address = serializers.CharField(label='Address', write_only=True)

    class Meta:
        model = Seller
        fields = [
            'id',
            'phone_number',
            'expire_date',
            'address',
            'account',
            'country',
            'city',
            'zip_code',
            'detail_address',
        ]

    def create(self, validated_data):
        try:
            with transaction.atomic():
                account_data = validated_data.pop('account')
                user = account_data.pop('user')
                user_obj = User.objects.create(**user)
                account = Account.objects.create(
                    user=user_obj,
                    **account_data
                )

                country_data = validated_data.pop('country')
                city_data = validated_data.pop('city')
                zip_code_data = validated_data.pop('zip_code')
                detail_address_data = validated_data.pop('detail_address')
                validated_data['address'] = "{}, {}, {}, {}".format(detail_address_data, city_data, country_data, zip_code_data)

                seller = Seller.objects.create(
                    account=account,
                    **validated_data
                )
        except IntegrityError:
            raise ValidationError("Custom Error, something went wrong.")
        return seller
