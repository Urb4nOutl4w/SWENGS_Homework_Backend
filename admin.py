from django.contrib import admin

# Register your models here.
from swengs.songs.models import Song, Artist


class SongAdmin(admin.ModelAdmin):
    pass


admin.site.register(Song, SongAdmin)

class ArtistAdmin(admin.ModelAdmin):
    pass


admin.site.register(Artist, ArtistAdmin)
