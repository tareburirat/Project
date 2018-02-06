from rest_framework import serializers

from apps.addresses.models import Address


class AddressSerializer(serializers.ModelSerializer):
    # street = serializers.CharField(write_only=True)
    address = serializers.CharField(write_only=True)
    sub_district = serializers.CharField(write_only=True)
    district = serializers.CharField(write_only=True)
    province = serializers.CharField(write_only=True)
    zip_code = serializers.CharField(write_only=True)


    class Meta:
        model = Address
        exclude = []
        extra_kwargs = {
            'address_details': {
                'read_only': True,
                'required': False
            }
        }

    def create(self, validated_data):
        address = validated_data.pop('address', None)
        sub_district = validated_data.pop('sub_district', None)
        district = validated_data.pop('district', None)
        province = validated_data.pop('province', None)
        zip_code = validated_data.pop('zip_code', None)
        validated_data['address_details'] = 'ที่อยู่ : ' + address
        validated_data['address_details'] += ' ,แขวง/ตำบล : ' + sub_district
        validated_data['address_details'] += ' ,เขต/อำเภอ : ' + district
        validated_data['address_details'] += ' ,จังหวัด : ' + province
        validated_data['address_details'] += ' ,ไปรษณี : ' + zip_code
        print(validated_data)
        return super(AddressSerializer, self).create(validated_data)