from django.core.exceptions import ValidationError
from django.db import transaction
from rest_framework import serializers

from apps.orders.models import Order, OrderItem
from apps.products.serializers import ProductSerializer
from apps.ratings.models import Rating


class SimpleOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = [
            'id',
            'order_number'
        ]


class OrderItemSerializer(serializers.ModelSerializer):
    product_data = serializers.SerializerMethodField()
    order = SimpleOrderSerializer(read_only=True)
    rating = serializers.IntegerField(required=False, write_only=True)

    class Meta:
        model = OrderItem
        exclude = []
        extra_kwargs = {
            'order': {
                'required': False
            }
        }

    def get_product_data(self, obj):
        return ProductSerializer(obj.product).data

    def update(self, instance, validated_data):
        if str(validated_data.get('rating', '')).isdigit():
            Rating.objects.create(
                rating=int(validated_data.get('rating')),
                seller_id=instance.product.seller_id,
                buyer_id=instance.order.buyer_id,
                order_item_id=instance.id
            )
        return super(OrderItemSerializer, self).update(instance, validated_data)


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        exclude = []

    def create(self, validated_data):
        try:
            with transaction.atomic():
                order_items = validated_data.pop('order_items')

                order = super(OrderSerializer, self).create(validated_data)

                for order_item in order_items:
                    OrderItem.objects.create(
                        order=order,
                        **order_item
                    )

        except KeyError:
            raise ValidationError('send the data properly')
        else:
            return order
