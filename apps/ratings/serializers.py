from rest_framework import serializers

from apps.ratings.models import Rating


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        exclude = []
