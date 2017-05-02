from django.conf.urls import url
from .views import register, user_login, user_logout
app_name = 'users'
urlpatterns = [
    url(r'^$', register, name='register'),
    url(r'^login/$', user_login,name='login'),
    url(r'^logout/', user_logout),
]
