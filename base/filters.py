import django_filters
from .models import Offer

class OfferFilter(django_filters.FilterSet):
    class Meta:
        model = Offer
        fields = {'position': ['icontains'],
                  'industry': ['exact'],
                  'city': ['icontains'],
                  'salary': ['gt']}