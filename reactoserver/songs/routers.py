#! -*- coding: utf-8 -*-

from swampdragon.route_handler import ModelRouter
from swampdragon import route_handler

from songs.serializers import SongSwampSerializer
from songs.models import Song


class SongRouter(ModelRouter):
    route_name = "song-router"
    model = Song
    serializer_class = SongSwampSerializer
    valid_verbs = ["subcribe", "unsubscribe", "get_object", "get_single",
        "get_list", ]

    def get_object(self, **kwargs):
        try:
            return self.model.objects.get(uuid=kwargs['uuid'])
        except self.model.DoesNotExist:
            return

    def get_query_set(self, **kwargs):
        return self.model.objects.all()


route_handler.register(SongRouter)
