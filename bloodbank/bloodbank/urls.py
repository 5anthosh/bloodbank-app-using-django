from django.conf.urls import url, include
from django.contrib import admin
from users.views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bloodbank/', include('login.urls'), name="register"),
    url(r'^register/', include('users.urls'), name='staffregister'),
    url(r'^staff/', home),
    url(r'^home/', include('users.urls2'))
]
