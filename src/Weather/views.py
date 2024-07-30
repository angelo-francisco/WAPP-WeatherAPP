from django.shortcuts import render
from weather.utils import get_weather, KelvinToCelsius
from time import strftime
from datetime import datetime

def main(request):
    if request.method == "GET":
        return render(request, 'pages/main.html')
    
    else:
        city = request.POST['city_name']
        weather = get_weather(city)
        date = strftime("%b %d, %I:%M%p")

        context = {
            'weather': weather, 
            'time': date,
            'feels_like': KelvinToCelsius(int(weather["main"]["feels_like"])),
            'desc': str(weather["weather"][0]["description"]).capitalize(),
            'main': str(weather["weather"][0]["main"]).capitalize(),
            'temp': KelvinToCelsius(int(weather["main"]["temp"])),
            'temp_max': KelvinToCelsius(int(weather["main"]["temp_max"])),
            'temp_min': KelvinToCelsius(int(weather["main"]["temp_min"])),
            'visible': float(weather["visibility"]) / 1000,
            'dt': datetime.fromtimestamp(weather["dt"]).strftime("%H:%M%p"),
            'rise': datetime.fromtimestamp(weather["sys"]["sunrise"]).strftime("%H:%M%p"),
            'set': datetime.fromtimestamp(weather["sys"]["sunset"]).strftime("%H:%M%p")
        }

        return render(request, 'pages/main.html', context=context)

