#! -*- codin: utf-8 -*-
import mimetypes
import datetime

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from mutagen.mp3 import MP3

SONGS_DIR = getattr(settings, "SONGS_STORAGE", getattr(settings, "MEDIA_ROOT"))


class Song(models.Model):
    """ Song model """
    ctime = models.DateField(auto_now_add=True)
    mtime = models.DateField(auto_now=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    duration = models.DurationField(default=datetime.timedelta)
    mime_type = models.CharField(_('mime type'), blank=True, max_length=256)
    cover = models.ImageField(
        max_length=255, null=True, default=None, blank=True)
    song_file = models.FileField(
        max_length=255, default=None, upload_to=SONGS_DIR)
    tags = ArrayField(
        models.CharField(max_length=100),
        blank=True,
        default=list
    )

    def __str__(self):
        return self.title


def get_mime_type(path):
    return mimetypes.guess_type(path)[0]


def get_song_lenght(path):
    mp3meta = MP3(path)
    if mp3meta.info:
        return datetime.timedelta(minutes=mp3meta.info.length)
    return datetime.timedelta


def set_metadata(sender, **kwargs):
    # Set song file mimetype on post_save signal
    changes = False
    instance = kwargs['instance']
    if instance.song_file:
        path = instance.song_file.path
    else:
        return
    mime_type = get_mime_type(path)
    duration = get_song_lenght(path)
    if instance.mime_type != mime_type:
        instance.mime_type = mime_type
        changes = True
    if instance.duration != duration:
        instance.duration = duration
        changes = True
    if changes:
        super(sender, instance).save()
    return

post_save.connect(set_metadata, sender=Song)
