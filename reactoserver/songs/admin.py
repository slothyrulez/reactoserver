from django.contrib import admin

from songs.models import Song


class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'duration', 'tags', 'uuid',)
    readonly_fields = ("duration", "mime_type", "uuid", )

admin.site.register(Song, SongAdmin)
