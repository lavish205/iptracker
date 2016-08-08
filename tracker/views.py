
import requests

from django.shortcuts import render_to_response
from django.template import RequestContext


def get_geolocation(request, ip=None):
    """
    get ip and return ip details rendered on map
    :param request:
    :param ip:
    :return:
    """
    template = 'index.html'
    HOST = 'http://ipinfo.io/'
    if ip:
        url = "{HOST}{ip}".format(HOST=HOST, ip=ip)
    else:
        url = HOST
    response = requests.get(url)

    data = response.json()
    if data:
        lat, lng = data.get('loc').split(',')
    else:
        lat, lng = 12.928562, 77.6135046

    ctx = {
        'lat': lat,
        'lng': lng,
        'network': data.get('org'),
        'city': data.get('city'),
        'region': data.get('region'),
        'hostname': data.get('hostname'),
        'ip': data.get('ip'),
        'country': data.get('country')
    }
    ctx = RequestContext(request, ctx)
    return render_to_response(template, ctx)

