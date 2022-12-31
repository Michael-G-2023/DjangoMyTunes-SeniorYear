from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import Count
from .models import Track, Artist, Album, Genre, Playlist

def home(request):
    return render(request,'tunes/home_page.html')

## Playlist Function ##
def browse_by_playlist(request):

    playlists = Playlist.objects.all()

    return render(request, 'tunes/playlist.html', {'playlists': playlists})

def detail_playlist(request, playlist_id):

    playlist = Playlist.objects.filter(playlist_id = playlist_id)
    tracks = playlist.tracks

    return render(request, 'tunes/playlistdetail.html', {'playlist': playlist, "tracks": tracks})


## Genre Functions ##
def browse_by_genre(request):

    genres = Genre.objects.all()

    return render(request, 'tunes/genre.html', {'genres': genres})

def detail_genre(request, genre_id):

    genre = Track.object.filter(genre_id = genre_id)

    return render(request, 'tunes/genredetail.html', {'genre': genre})


## Artist Functions ## 
def browse_by_artist(request):

    artists = Artist.objects.all().annotate(tracks = Count('album__track'))
   
    return render(request, 'tunes/artist.html', context = {'artists': artists})

def detail_artist(request, artist_id):
    trackslist = Track.objects.filter(album__artist_id = artist_id)
    albumslist = Album.objects.filter(artist_id = artist_id)
    return render(request, 'tunes/artistdetail.html', context = {'tracks': trackslist, 'albums':albumslist})

## Album Funtions ##
def browse_by_album(request):

    albums = Album.objects.all().annotate(numtracks = Count('track'))

    return render(request, 'tunes/album.html', context =  {'albums': albums})
    
def detail_album(request, album_id):

    album = Album.objects.filter(album_id = album_id)

    return render(request, 'tunes/albumdetail.html', {"album": album})

## Track Functions ##
def browse_by_track(request):

    tracks = Track.objects.all()

    return render(request, 'tunes/album.html', {'tracks': tracks})

