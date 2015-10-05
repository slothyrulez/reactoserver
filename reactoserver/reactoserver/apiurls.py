from django.conf.urls import url, include
from rest_framework import routers

from songs.api import SongsViewSet
from playerstatus.api import PlayerStatusViewSet

router = routers.DefaultRouter()
router.register(r'songs', SongsViewSet)
router.register(r'playerstatus', PlayerStatusViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
