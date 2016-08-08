from django.conf.urls.defaults import patterns, url

from tracker.views import get_geolocation

urlpatterns = patterns('',
                       url(r'^track-ip/(?P<ip>((2[0-5]|1[0-9]|[0-9])?[0-9]\.){3}((2[0-5]|1[0-9]|[0-9])?[0-9]))/$', get_geolocation,
                           name='track-ip'),
                       url(r'^track-ip/$', get_geolocation,
                           name='track-ip'),
    )