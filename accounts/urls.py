from django.conf.urls import patterns, include, url
from .views import (
    DashboardView,
    UserProfileView,
)


urlpatterns = patterns('',
    url(r'^dashboard$', DashboardView.as_view(), name='dashboard'),
    url(r'^profile$', UserProfileView.as_view(), name='user_profile'),
)
