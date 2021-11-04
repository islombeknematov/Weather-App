import urllib.request

from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.

import json


def get_weather(request):
    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=742370029c8ae0a47ccf91b8a42156fd').read()

        list_data = json.loads(source)
        # print(list_data)
        data = {
            "country_name": str(list_data['name']),
            "country_code": str(list_data['sys']['country']),

            "coord_lon": str(list_data['coord']['lon']) + ' longitude',
            "coord_lat": str(list_data['coord']['lat']) + ' latitude',

            "temperature": str(list_data['main']['temp']) + ' `C',
            # "time": str(list_data['timezone']),
        }

    else:
        data = dict()

    return render(request, 'WeatherApp.html', data)
