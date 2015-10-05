# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=100), default=list, blank=True),
        ),
    ]
