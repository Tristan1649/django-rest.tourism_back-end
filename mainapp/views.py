from rest_framework.viewsets import ModelViewSet
from .models import Location, Tur, Gallery, Event
from .serializers import LocationSerializer, TurSerializer, GallerySerializer, EventSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]

class TurViewSet(ModelViewSet):
    queryset = Tur.objects.all()
    serializer_class = TurSerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]

class GalleryViewSet(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]