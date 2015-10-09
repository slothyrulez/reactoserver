from rest_framework import viewsets

from songs.serializers import SongRestSerializer
from songs.models import Song


class SongsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows songs to be viewed or edited.
    """
    queryset = Song.objects.all().order_by('-ctime')
    serializer_class = SongRestSerializer
