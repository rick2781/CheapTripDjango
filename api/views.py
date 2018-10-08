from django.shortcuts import render

from .models import Flight, User
from rest_framework import viewsets, permissions, filters
from api.serializers import FlightSerializer, UserSerializer

from .permissions import IsOwnerOrReadOnly

from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class FlightViewSet(viewsets.ModelViewSet):

    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                            IsOwnerOrReadOnly,)

    filter_backends = (DjangoFilterBackend,
                        filters.SearchFilter,)
    filter_fields = ('destination',)
    search_fields = ('destination', 'owner__username',)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
