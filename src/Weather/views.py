from django.shortcuts import render
from utils import get_weather

def main(request):
    if request.method == "GET":
        return render(request, 'pages/main.html')
    
    else:
        city = request.POST['city_name']
        weather = get_weather(city)

        return render(request, 'pages/main.html', context={'weather': weather})

