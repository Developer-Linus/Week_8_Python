import urllib.request # This is a module that enables the sending of requests to the API we'll be creating.

import json # Handles the nature of the data we'll be receiving from our requests.

from django.shortcuts import render
import os
from dotenv import load_dotenv

# Load environment variables from environment variables
load_dotenv()

# Access the environment variables 
api_key = os.getenv("WEATHER_API")

# Create your views here.

def index(request):
    
    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}").read()
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)



