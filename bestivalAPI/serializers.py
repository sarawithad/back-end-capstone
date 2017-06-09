from rest_framework import serializers
from bestivalAPI.models import *

class FestivalSerializer(serializers.HyperLinkedModelSerializer):
    """
    """
    class Meta:
        model = Festival
        fields = ('url','festival_name', 'date', 'location', 'environment')


class FestivalGenreSerializer(serializers.HyperLinkedModelSerializer):
    """
    """
    class Meta:
        model = FestivalGenre
        fields = ('url', 'festival', 'genre')


class FestivalArtistSerializer(serializers.HyperLinkedModelSerializer):
    """
    """
    class Meta:
        model = FestivalArtist
        fields = ('url', 'festival', 'artist')


class GenreSerializer(serializers.HyperLinkedModelSerializer):
    """
    """
    class Meta:
        model = Genre
        fields = ('url', 'genre_name')


class ArtistSerializer(serializers.HyperLinkedModelSerializer):
    """
    """
    class Meta:
        model = Artist
        fields = ('url', 'artist_name', 'genre')


class LocationSerializer(serializers.HyperLinkedModelSerializer):
    """
    """
    class Meta:
        model = Location
        fields = ('url', 'state')


class DateSerializer(serializers.HyperLinkedModelSerializer):
    """
    """
    class Meta:
        model = Date
        fields = ('url', 'month', 'year')


class EnvironmentSerializer(serializers.HyperLinkedModelSerializer):
    """
    """
    class Meta:
        model = Environment
        fields = ('url', 'environment_type')











