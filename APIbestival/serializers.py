from rest_framework import serializers
from APIbestival.models import *
from django.contrib.auth.models import User, Group

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    class Meta:
        model = Location
        fields = ('url', 'state_name')

class FestivalSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    location = serializers.StringRelatedField()
    artists = serializers.StringRelatedField(many=True)
    genres = serializers.StringRelatedField(many=True)
    date = serializers.StringRelatedField()


    class Meta:
        model = Festival
        fields = ('url','festival_name', 'date', 'location', 'artists', 'genres', 'festival_website')


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




class DateSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    class Meta:
        model = Date
        fields = ('url', 'month', 'year')









