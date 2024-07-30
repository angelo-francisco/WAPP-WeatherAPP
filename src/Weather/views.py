from django.shortcuts import render


def main(request):
    if request.method == "GET":
        return render(request, 'pages/main.html')
    
    else:
        city = request.POST['city_name']

        return render(request, 'pages/main.html', context=context)

def handler404(request, exception):
    return render(request, 'error/404.html')

def handler500(request):
    return render(request, 'error/500.html', status=500)