import mimetypes

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _


class Song(models.Model):
    """ Song model """
    ctime = models.DateField(auto_now_add=True)
    mtime = models.DateField(auto_now=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    duration = models.DurationField(default=0)
    mime_type = models.CharField(_('mime type'), blank=True, max_length=256)
    cover = models.ImageField(max_length=255, null=True, default=None)
    song_file = models.ImageField(max_length=255, default=None)
    tags = ArrayField(
        models.CharField(max_length=100),
        blank=True,
        default=list
    )


def get_mime_type(path):
    return mimetypes.guess_type(path)[0]


def set_mimetype(sender, **kwargs):
    # Set song file mimetype on post_save signal
    instance = kwargs['instance']
    if instance.song_file:
        path = instance.song_file.path
    else:
        return
    mime_type = get_mime_type(path)
    if instance.mime_type == mime_type:
        return
    else:
        instance.mime_type = get_mime_type(path)
        super(sender, instance).save()

post_save.connect(set_mimetype, sender=Song)
