from rest_framework import viewsets

from playerstatus.serializers import PlayerStatusSeriazer
from playerstatus.models import PlayerStatus


class PlayerStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows songs to be viewed or edited.
    """
    queryset = PlayerStatus.objects.all().order_by('-ctime')
    serializer_class = PlayerStatusSeriazer
