from rest_framework import serializers

from apps.transactions.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        exclude = []
