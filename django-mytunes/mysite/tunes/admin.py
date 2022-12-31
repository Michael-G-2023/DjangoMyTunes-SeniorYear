from django.contrib import admin

# Register your models here.
from .models import Artist
from .models import Album
from .models import Genre
from .models import Track
from .models import Playlist

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Track)
admin.site.register(Playlist)
