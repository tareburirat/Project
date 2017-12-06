from rest_framework import serializers

from apps.addresses.models import Address

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        exclude = []