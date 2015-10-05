# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_song_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='cover',
            field=models.ImageField(max_length=255, default=None, upload_to='', null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='mime_type',
            field=models.CharField(max_length=256, verbose_name='mime type', blank=True),
        ),
        migrations.AddField(
            model_name='song',
            name='song_file',
            field=models.ImageField(max_length=255, default=None, upload_to=''),
        ),
    ]
