from django.conf.urls.defaults import patterns, url

from tracker.views import get_geolocation

urlpatterns = patterns('',
                       url(r'^track-ip/(.*)/$', get_geolocation,
                           name='track-ip'),
                       url(r'^track-ip/$', get_geolocation,
                           name='track-ip'),
    )