from django.shortcuts import render
# Create your views here.

def show_main(request):
    context = {
        'app_name' : 'vin-shop',
        'name': 'Kevin Adriano',
        'npm': '2306172552',
        'class': 'PBP KKI',
    }

    return render(request, "main.html", context)