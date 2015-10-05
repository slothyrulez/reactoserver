# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
from django.contrib.postgres.operations import HStoreExtension
import django.contrib.postgres.fields.hstore


class Migration(migrations.Migration):

    dependencies = [
        # HStoreExtension(),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerStatus',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, default=uuid.uuid4)),
                ('ctime', models.DateField(auto_now_add=True)),
                ('mtime', models.DateField(auto_now=True)),
                ('volume', models.IntegerField()),
                ('actualsong', django.contrib.postgres.fields.hstore.HStoreField()),
            ],
        ),
    ]
