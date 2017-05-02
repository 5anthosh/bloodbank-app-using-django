from django.conf.urls import url
from .views import public_home, search, details, storage

urlpatterns = [
    url(r'^$', public_home),
    url(r'^search/', search),
    url(r'^details/', details),
    url(r'^storage/', storage),
]
