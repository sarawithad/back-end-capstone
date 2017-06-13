from rest_framework import serializers
from APIbestival.models import *
from django.contrib.auth.models import User, Group

class FestivalSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    class Meta:
        model = Festival
        fields = ('url','festival_name', 'date', 'location')


class FestivalGenreSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    class Meta:
        model = FestivalGenre
        fields = ('url', 'festival', 'genre')


class FestivalArtistSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    class Meta:
        model = FestivalArtist
        fields = ('url', 'festival', 'artist')


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    class Meta:
        model = Genre
        fields = ('url', 'genre_name')


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    class Meta:
        model = Artist
        fields = ('url', 'artist_name', 'genre')


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    class Meta:
        model = Location
        fields = ('url', 'state_name')


class DateSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    class Meta:
        model = Date
        fields = ('url', 'month', 'year')









