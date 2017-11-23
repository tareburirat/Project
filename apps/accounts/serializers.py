from rest_framework import serializers

from apps.accounts.models import Account

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        exclude = []
