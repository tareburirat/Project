from rest_framework import serializers

from apps.values.models import Value


class ValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Value
        exclude = []
