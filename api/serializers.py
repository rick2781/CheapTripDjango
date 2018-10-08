from .models import Flight
from rest_framework import serializers
from django.contrib.auth.models import User

class FlightSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Flight
        fields = ('id',
        'placeIcon',
        'origin',
        'destination',
        'departure',
        'arrival',
        'price',
        'owner',
        'owner_id')

class UserSerializer(serializers.ModelSerializer):
    flights = serializers.PrimaryKeyRelatedField(many=True, queryset=Flight.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'flights')
