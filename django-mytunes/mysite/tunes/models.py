from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models



# Create your models here.
class Artist(models.Model):

    name = models.CharField(max_length = 120)
    
    def __str__(self):
        return self.name

class Album(models.Model):

    title = models.CharField(max_length = 160)
    artist = models.ForeignKey(Artist, null = True, blank = True, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Genre(models.Model):

    name = models.CharField(max_length = 120)
    
    def __str__(self):
        return self.name
    
class Track(models.Model):

    name = models.CharField(max_length = 200)
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    genre = models.ForeignKey(Genre, null = True, blank = True, on_delete = models.SET_NULL)
    composer = models.CharField(null = True, blank = True, max_length = 220)
    milliseconds = models.IntegerField()

    def __str__(self):
        return self.name
    
    
class Playlist(models.Model):

    name = models.CharField(max_length = 120)
    tracks = models.ManyToManyField(Track)

    def __str__(self):
        return self.name