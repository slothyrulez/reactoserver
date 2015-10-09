# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_auto_20151008_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='cover',
            field=models.ImageField(max_length=255, null=True, default=None, upload_to='', blank=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.DurationField(default=datetime.timedelta),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_file',
            field=models.FileField(max_length=255, default=None, upload_to='/home/slothy/dev/a_player_project/reactoserver/reactoserver/medias/songs'),
        ),
    ]
