from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db import transaction
from rest_framework import serializers

from apps.accounts.models import Account


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()

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
