from django.forms import ModelForm
from .models import Offer


class OfferForm(ModelForm):
    class Meta:
        model = Offer
        fields = '__all__'