from django.db import transaction
from rest_framework import serializers

from apps.products.models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(required=False, queryset=Product.objects.all())
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ['product', 'image']

    def get_image(self, obj):
        return "http://localhost:8000/" + obj.image.url


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    property = serializers.SerializerMethodField()
    first_image_url = serializers.SerializerMethodField()
    freight_detail = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = []


    @staticmethod
    def get_property(obj):
        return obj.properties

    @staticmethod
    def get_first_image_url(obj):
        first_image = obj.images.first()
        if first_image is None:
            return ""
        else:
            return "http://localhost:8000/" + first_image.image.url

    @staticmethod
    def get_freight_detail(obj):
        return obj.get_freight_display()
