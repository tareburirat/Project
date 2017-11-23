from rest_framework import viewsets

from apps.ratings.models import Rating
from apps.ratings.serializers import RatingSerializer



class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()