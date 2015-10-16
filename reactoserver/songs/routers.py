#! -*- coding: utf-8 -*-
import uuid
import itertools

from swampdragon.route_handler import ModelRouter
from swampdragon import route_handler

from songs.serializers import SongSwampSerializer
from songs.models import Song


# class SongRouter(ModelRouter):
#     route_name = "song-router"
#     model = Song
#     serializer_class = SongSwampSerializer
#     valid_verbs = ["subcribe", "unsubscribe", "get_object", "get_single",
#         "get_list", ]
#
#     def get_object(self, **kwargs):
#         try:
#             return self.model.objects.get(uuid=kwargs['uuid'])
#         except self.model.DoesNotExist:
#             return
#
#
#     def get_query_set(self, **kwargs):
#         return self.model.objects.all()


class ChunkedFieldsAwareModelRouter(ModelRouter):
    def _gen_chunked_id(self):
        return str(uuid.uuid4())

    def _prepare_first(self):
        _aux = dict(self._serialized)
        _aux.update({
            "chunked_first": True,
            "chunked_response": {
                "chunked_id": self._chunked_id,
                "chunk_num": next(self._chunk_counter),
                "chunk_total": self._chunked_info["chunk_total"],
                "chunk": list(next(self._gen_chunked)),
            }
        })
        return _aux

    def _prepare_middle(self, data):
        return {
            "chunked_middle": True,
            "chunked_id": self._chunked_id,
            "chunk_num": next(self._chunk_counter),
            "chunk_total": self._chunked_info["chunk_total"],
            "chunk": list(data),
        }

    def _prepare_last(self):
        return {
            "chunked_last": True,
            "chunked_id": self._chunked_id,
        }


    def _test_chunked(self, func, obj):
        return func(obj)

    def _get_chunked_info(self, obj, serializer, chunked_field):
        try:
            return getattr(serializer,
                "chunked_" + chunked_field + "_info", None)(obj)
        except TypeError:
            raise NotImplementedError

    def send_chunked(self, obj, chunked_field, **kw):
        self.serializer = self.serializer_class(instance=obj)
        self._chunked_info = self._get_chunked_info(obj, self.serializer, chunked_field)
        self._serialized = self.serializer.serialize()

        # Here instead of the serialized data, we have a generator yielding
        # the chunks of the chunked field
        self._chunk_counter = itertools.count(0, 1)
        self._chunked_id = self._gen_chunked_id()
        self._gen_chunked = self._serialized.pop(chunked_field)

        self.send(self._prepare_first(), **kw)
        # Chunked generator already started
        for data_chunk in self._gen_chunked:
            self.send(self._prepare_middle(data_chunk), **kw)
        self.send(self._prepare_last(), **kw)


    def send_single(self, obj, **kwargs):
        self.serializer = self.serializer_class(instance=obj)
        _go_chunked = False
        _chunked_field = getattr(self.serializer.Meta, "chunked_field", None)
        if _chunked_field:
            _test_func = getattr(self.serializer,
                "test_chunked_" + _chunked_field, None)
            if _test_func:
                _go_chunked = self._test_chunked(_test_func, obj)
            else:
                raise NotImplementedError
        else:
            raise NotImplementedError

        if _go_chunked:
            self.send_chunked(obj, _chunked_field, **kwargs)
        else:
            self.send(self.serializer.serialize(), **kwargs)


class SongRouter(ChunkedFieldsAwareModelRouter):
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
