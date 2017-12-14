from django.contrib.auth.models import User
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

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        User.objects.create_user(username, password=password)
        return super(AccountSerializer, self).create(**validated_data)
