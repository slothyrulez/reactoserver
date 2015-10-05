# rest_framework_hstore
from rest_framework import serializers
from rest_framework_hstore.fields import HStoreField

from playerstatus.models import PlayerStatus


class PlayerStatusSeriazer(serializers.ModelSerializer):
    actualsong = HStoreField

    class Meta:
        model = PlayerStatus
        fields = ('volume', 'actualsong',)
