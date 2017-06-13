from django.shortcuts import render
from django.contrib.auth.models import *
from rest_framework import viewsets
from APIbestival.serializers import *
from APIbestival.models import *

class FestivalViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Festival.objects.all().order_by('festival_name')
    serializer_class = FestivalSerializer


class GenreViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Genre.objects.all().order_by('genre_name')
    serializer_class = GenreSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Artist.objects.all().order_by('artist_name')
    serializer_class = ArtistSerializer


class LocationViewSet(viewsets.ModelViewSet):
    """
    Purpose: expose festival location data to client
    Author: Dara Thomas
    """
    queryset = Location.objects.all().order_by('state_name')
    serializer_class = LocationSerializer    

class DateViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Date.objects.all().order_by('month')
    serializer_class = DateSerializer


# class EnvironmentViewSet(viewsets.ModelViewSet):
#     """
#     """
#     queryset = Environment.objects.all().order_by('environment_type')
#     serializer_class = EnvironmentSerializer