from django.shortcuts import render

from .models import Flight
from rest_framework import viewsets
from api.serializers import FlightSerializer

# Create your views here.
class FlightViewSet(viewsets.ModelViewSet):

    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
