from django.conf.urls import patterns, include, url
from .views import (
    IndexView,
    LoginView,
    LogoutView,
)


urlpatterns = patterns('',

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login$', LoginView.as_view(), name='user_login'),
    url(r'^logout$', LogoutView.as_view(), name='user_logout'),
)
