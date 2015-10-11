# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0006_song_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='uuid',
            field=models.UUIDField(db_index=True, editable=False, default=uuid.uuid4),
        ),
    ]
