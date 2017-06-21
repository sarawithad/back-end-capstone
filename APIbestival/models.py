from django.db import models

class Location(models.Model):
    """
    Purpose: expose festival location data to client
    Author: Dara Thomas
    """
    state_name = models.CharField(max_length=2)

    def __str__(self):
        return self.state_name


class Date(models.Model):
    """
    Purpose: expose festival date data to client
    Author: Dara Thomas
    """
    month =  models.CharField(max_length=15)
    year = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.month, self.year)

class Festival(models.Model):
    """
    Purpose: expose specific festival data to client
    Author: Dara Thomas
    """
    festival_name = models.CharField(max_length = 30)
    date = models.ForeignKey(Date)    
    location = models.ForeignKey(Location)
    artists = models.ManyToManyField("Artist", through="FestivalArtist")
    genres = models.ManyToManyField("Genre", through="FestivalGenre")



class Genre(models.Model):
    """
    Purpose: expose festival genre data to client
    Author: Dara Thomas
    """
    genre_name = models.CharField(max_length=20)

    def __str__(self):
        return self.genre_name

class Artist(models.Model):
    """
    Purpose: expose festival artist data to client
    Author: Dara Thomas
    """
    artist_name = models.CharField(max_length=20)
    genre = models.ForeignKey(Genre)

    def __str__(self):
        return self.artist_name


class FestivalGenre(models.Model):
    """
    Purpose: expose data for which festivals play which genre of music to client
    Author: Dara Thomas
    """
    festival = models.ForeignKey(Festival)
    genre = models.ForeignKey(Genre)


class FestivalArtist(models.Model):
    """
    Purpose: expose data for which festivals play which artists to client
    Author: Dara Thomas
    """
    festival = models.ForeignKey(Festival)
    artist = models.ForeignKey(Artist)   
