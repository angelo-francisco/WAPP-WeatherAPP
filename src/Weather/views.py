from django.shortcuts import render, redirect
from core.settings import API_KEY
import requests
import time

    
def main(request):
    if request.method == "GET":
        return render(request, 'pages/main.html')
    
    else:
        city = request.POST['city_name']
        link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        request_api = requests.get(link)
        request_api_dict = request_api.json()

        context = {
            'data': time.strftime('%B %d'),
            'hora': time.strftime('%I:%M %p'),
            'request_api': request_api,
            'code': request_api_dict['cod'],
            'city': city,
            'lon': f'{float(request_api_dict['coord']['lon']):.2f}',
            'lat': f'{float(request_api_dict['coord']['lat']):.2f}',
            'main': request_api_dict['weather'][0]['main'],
            'description': request_api_dict['weather'][0]['description'],
            'temp': f'{float(request_api_dict['main']['temp'] - 273.15):.2f}',
            'pressure': request_api_dict['main']['pressure'],
            'humidity': request_api_dict['main']['humidity'],
            'country': request_api_dict['sys']['country']
        }
        print(request_api_dict['weather'][0]['main'])
        return render(request, 'pages/main.html', context=context)

def handler404(request, exception):
    return render(request, 'error/404.html')

def handler500(request):
    return render(request, 'error/500.html', status=500)