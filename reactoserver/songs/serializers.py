#! -*- coding: utf-8 -*-

from rest_framework import serializers as rest_serializers
from swampdragon.serializers.model_serializer import ModelSerializer

from songs.models import Song


class SongRestSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'uuid', 'author', 'duration', 'tags')


class SongSwampSerializer(ModelSerializer):
    class Meta:
        model = Song
        publish_fields = ('song_file', 'mime_type', 'uuid', )

    def serialize_song_file(self, obj):
        # Keeping simple
        # if obj.song_file.multiple_chunks():
            # return obj.song_file.chunks()
        _aux = obj.song_file.read()
        return list(_aux)

    def serialize_uuid(slef, obj):
        return str(obj.uuid)
