from django.urls import path

from . import views

app_name = 'tunes'
urlpatterns = [    
    path('', views.home, name='home'),

    path('artist/', views.browse_by_artist, name = 'all_artists'),
    path('artist/<int:artist_id>', views.detail_artist, name = 'specific_artist'),

    path('album/', views.browse_by_album, name = 'all_albums'),
    path('album/<int:album_id>', views.detail_album, name = "specific_album"),

    path('genre/', views.browse_by_genre, name = 'all_genres'),
    path('genre/<int:genre_id>', views.detail_genre, name = "specific_genre"),

    path('playlist/', views.browse_by_playlist, name = 'all_playlists'),
    path('playlist/<int:playlist_id>/', views.detail_playlist, name = 'specific_playlist'),

    path('track/', views.browse_by_track, name = 'all_tracks'),
]