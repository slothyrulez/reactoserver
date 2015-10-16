#! -*- coding: utf-8 -*-

from rest_framework import serializers as rest_serializers
from swampdragon.serializers.model_serializer import ModelSerializer

from songs.models import Song


class SongRestSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'uuid', 'author', 'duration', 'tags')


# class SongSwampSerializer(ModelSerializer):
#     class Meta:
#         model = Song
#         publish_fields = ('song_file', 'mime_type', 'uuid', )
#
#     def serialize_song_file(self, obj):
#         # Keeping simple
#         # if obj.song_file.multiple_chunks():
#         #     # return obj.song_file.chunks()
#         # _aux = obj.song_file.read()
#         # return list(_aux)
#         _aux = obj.song_file.read()
#         return obj.song_file.read()
#         # The idea:
#         # Send a custom "list" of messages handling the chunks sending
#
#     def serialize_uuid(slef, obj):
#         return str(obj.uuid)
#

# ModelWithChunkedField
# ChunkedFieldSerializer
_cached  = {}

class ModelChunkedSerializer(ModelSerializer):
    pass

class SongSwampSerializer(ModelChunkedSerializer):
    class Meta:
        model = Song
        publish_fields = ('song_file', 'mime_type', 'uuid', )
        chunked_field = 'song_file'

    def test_chunked_song_file(self, obj):
        return obj.song_file.multiple_chunks()

    def chunked_song_file_info(self, obj):
        _fsize = obj.song_file.size
        _csize = obj.song_file.DEFAULT_CHUNK_SIZE
        _num_chunks = _fsize // _csize
        _num_chunks += 1 if (_fsize / _csize is not 0) else 0
        return {
            u"multiple_chunks": obj.song_file.multiple_chunks(),
            u"chunk_size": _csize,
            u"chunk_total":  _num_chunks,
            u"size": _fsize
        }

    def serialize_song_file(self, obj):
        if obj.song_file.multiple_chunks():
            return obj.song_file.chunks()  # Generator
        return list(obj.song_file.read())  # Whole

    def serialize_uuid(slef, obj):
        return str(obj.uuid)
