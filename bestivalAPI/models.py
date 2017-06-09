from django.db import models

class Festival(models.model):
    """
    Purpose: expose specific festival data to client
    Author: Dara Thomas
    """
    festival_name = models.CharField(max_length = 30)
    date = models.ForeignKey(Date)    
    location = models.ForeignKey(Location)
    environment = models.ForeignKey(Environment)


class FestivalGenre(models.model):
    """
    Purpose: expose data for which festivals play which genre of music to client
    Author: Dara Thomas
    """
    festival = models.ForeignKey(Festival)
    Genre = models.ForeignKey(Genre)


class FestivalArtist(models.model):
    """
    Purpose: expose data for which festivals play which artists to client
    Author: Dara Thomas
    """
    festival = models.ForeignKey(Festival)
    artist = models.ForeignKey(Artist)   


class Genre(models.model):
    """
    Purpose: expose festival genre data to client
    Author: Dara Thomas
    """
    genre_name = models.CharField(max_length=20)


class Artist(models.model):
    """
    Purpose: expose festival artist data to client
    Author: Dara Thomas
    """
    artist_name = models.CharField(max_length=20)
    genre = models.ForeignKey(Genre)


class Location(models.model):
    """
    Purpose: expose festival location data to client
    Author: Dara Thomas
    """
    state: models.CharField(max_length=2)


class Date(models.model):
    """
    Purpose: expose festival date data to client
    Author: Dara Thomas
    """
    month: models.CharField(max_length=15)
    year: models.IntegerField()


class Environment(models.model):
    """
    Purpose: expose festival environment data to client
    Author: Dara Thomas
    """
    environment_type: models.CharField(max_length=20)


