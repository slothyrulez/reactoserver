from django.contrib import admin

from songs.models import Song


class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'duration')
    readonly_fields = ("duration", "mime_type", )

admin.site.register(Song, SongAdmin)
