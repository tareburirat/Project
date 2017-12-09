from django.core.exceptions import ValidationError
from rest_framework import serializers

from apps.accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = [
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'display_name',
        ]
