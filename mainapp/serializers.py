from rest_framework import serializers
from .models import Location, Tur, Gallery, Event

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'title', 'image', 'desc', 'maps', 'history')

class TurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tur
        fields = ('id', 'title', 'location', 'desc', 'price', 'duration', 'ocupation')

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('id', 'title', 'image', 'location')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'image', 'duration')