from .models import Flight
from rest_framework import serializers

class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = ('id',
        'placeIcon',
        'origin',
        'destination',
        'departure',
        'arrival',
        'price')
