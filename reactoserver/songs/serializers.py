#! -*- coding: utf-8 -*-

import json

from rest_framework import serializers as rest_serializers
from swampdragon.serializers.model_serializer import ModelSerializer
from swampdragon.serializers.field_deserializers import (
    BaseFieldDeserializer, register_field_deserializer)

from songs.models import Song


def to_json(python_obj):
    if isinstance(python_obj, bytes):
        return list(python_obj)


class SongRestSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'author', 'duration', 'tags')


class SongSwampSerializer(ModelSerializer):
    class Meta:
        model = Song
        publish_fields = ('song_file', 'mime_type', )

    def serialize_song_file(self, obj):
	# Keeping simple
        # if obj.song_file.multiple_chunks():
            # return obj.song_file.chunks()
        _aux = obj.song_file.read()
        return list(_aux)
