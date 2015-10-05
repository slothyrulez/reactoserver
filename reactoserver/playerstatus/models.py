import uuid

from django.db import models
from django.contrib.postgres.fields import HStoreField


class PlayerStatus(models.Model):
    """ Model persist player status """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ctime = models.DateField(auto_now_add=True)
    mtime = models.DateField(auto_now=True)
    volume = models.IntegerField()
    actualsong = HStoreField()
