from django.conf.urls import url
from .views import add_donar, search, detail, donate, blood_storage, records

urlpatterns = [
    url(r'^register/$', add_donar),
    url(r'^$', search),
    url(r'^search/$', detail),
    url(r'^donate/$', donate),
    url(r'^blood/', blood_storage),
    url(r'^records/', records)
]
