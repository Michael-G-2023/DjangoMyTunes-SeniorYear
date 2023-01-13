from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.db.models import Count
import sqlite3
from django.contrib.auth.models import User

from .models import Track, Artist, Album, Genre, Playlist, SharedRequest
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'tunes/home_page.html')

## Playlist Function ##
@login_required(login_url = "/accounts/login/")

def browse_by_playlist(request):
    errormessage = ""
    if request.method == "POST" and Playlist.objects.filter(name = request.POST['name'], user = request.user).count() > 0:
        errormessage = "You already have a playlist by that name, please choose a diffferent name."
    elif request.method == "POST":
        newp = Playlist(name = request.POST["name"], user = request.user)
        newp.save()

    playlists = list(Playlist.objects.filter(user = request.user))
    sharedplaylists = list(Playlist.objects.filter(shared_with = request.user))
    return render(request, 'tunes/playlist.html', {'playlists': playlists, 'msg':errormessage, "shared": sharedplaylists})

def detail_playlist(request, playlist_id):
    if request.method == "POST":
        Playlist.objects.get(id = playlist_id).tracks.add(Track.objects.get(id = request.POST["track"]))
    playlist = Playlist.objects.get(id = playlist_id)
    tracks = list(Track.objects.all())

    return render(request, 'tunes/playlistdetail.html', {'playlist': playlist, 'tracks':tracks})


## Genre Functions ##
def browse_by_genre(request):

    genres = list(Genre.objects.all())

    return render(request, 'tunes/genre.html', {'genres': genres})

def detail_genre(request, genre_id):

    genretracks = list(Track.objects.filter(genre_id = genre_id))

    return render(request, 'tunes/genredetail.html', {'genre': genretracks})


## Artist Functions ## 
def browse_by_artist(request):
    artists = Artist.objects.all().annotate(tracks = Count('album__track'))
    return render(request, 'tunes/artist.html', context = {'artists': artists})

def detail_artist(request, artist_id):
    trackslist = list(Track.objects.filter(album__artist_id = artist_id))
    albumslist = list(Album.objects.filter(artist_id = artist_id))
    artist = Artist.objects.get(id = artist_id)
    return render(request, 'tunes/artistdetail.html', context = {'trackslist': trackslist, 'albumslist':albumslist, 'artist':artist})

## Album Funtions ##
def browse_by_album(request):

    albums = Album.objects.all().annotate(numtracks = Count('track'))

    return render(request, 'tunes/album.html', context =  {'albums': albums})
    
def detail_album(request, album_id):

    album = Album.objects.get(id = album_id)

    return render(request, 'tunes/albumdetail.html', context = {"album": album})

## Track Functions ##
def browse_by_track(request):
    tracks = list(Track.objects.all())
    
    return render(request, 'tunes/track.html', {'tracks': tracks})


def detail_track(request, track_id):

    track = Track.objects.get(id = track_id)

    return render(request, 'tunes/trackdetail.html', {'track': track})

"""
def shareanyplaylist(request):
    playlistList = Playlist.objects.filter(user = request.user)
    return render(request, "tunes/share.html", {'playlists': playlistList})
"""
def shareplaylist(request, playlist_id):
    if request.method == "POST":
        Playlist.objects.get(id = playlist_id).shared_with.add(User.objects.get(id = request.POST["name"]))
    allusers = User.objects.exclude(id = request.user.id)
    playlist = Playlist.objects.get(id = playlist_id)
    return render(request, 'tunes/sharespecific.html', {'playlist': playlist, 'allusers':allusers})

def socials(request):
    if request.method == "POST":
        SharedRequest