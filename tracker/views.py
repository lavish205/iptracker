
import requests

from django.shortcuts import render_to_response
from django.template import RequestContext


def get_geolocation(request, ip=None):
    template = 'index.html'
    HOST = 'http://ipinfo.io/'
    if ip:
        url = "{HOST}{ip}".format(HOST=HOST, ip=ip)
    else:
        url = HOST
    response = requests.get(url)
    data = response.json()

    lat, lng = data.get('loc').split(',')

    ctx = {
        'lat': lat,
        'lng': lng
    }
    ctx = RequestContext(request, ctx)
    return render_to_response(template, ctx)

