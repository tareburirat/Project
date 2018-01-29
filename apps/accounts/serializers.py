from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db import transaction
from rest_framework import serializers

from apps.accounts.models import Account
from apps.addresses.models import Address


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    cart_products = serializers.SerializerMethodField()
    primary_address = serializers.SerializerMethodField()

    class Meta:
        model = Account
        exclude = []

    def create(self, validated_data):
        try:
            with transaction.atomic():
                user = validated_data.pop('user')
                print(validated_data)
                user_obj = User.objects.create_user(**user)
                account = Account.objects.create(
                    user=user_obj,
                    **validated_data
                )
        except IntegrityError:
            raise ValidationError("Username Exist")
        return account

    @staticmethod
    def get_cart_products(obj):
        return obj.cart_set.values_list('product__id', flat=True)

    @staticmethod
    def get_primary_address(obj):
        try:
            primary_address = obj.address_set.get(primary=True)
            return primary_address.address_details
        except (Address.DoesNotExist, Address.MultipleObjectsReturned):
            return ""
