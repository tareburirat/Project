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

    class Meta:
        model = Product
        exclude = []

    @staticmethod
    def get_property(obj):
        return obj.properties