import urllib.request

from django.shortcuts import render

# Create your views here.

import json


def get_weather(request):
    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=742370029c8ae0a47ccf91b8a42156fd').read()

        list_data = json.loads(source)

        data = {
            "country_code": str(list_data['sys']['country']),
            "coordinate": str(list_data['coord']['lon']) + ' lon' + ', '
                          + str(list_data['coord']['lat']) + ' lat',
            "temperature": str(list_data['main']['temp']) + ' `C',
        }

        print(data)
    else:
        data = dict()

    return render(request, 'WeatherApp.html', data)
