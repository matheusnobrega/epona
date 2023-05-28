from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from city.models import City
from attraction.models import Hotel, Restaurant
from client.models import Client
from package.models import Package
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Count
from django.urls import reverse

def index(request):

    if request.method == 'POST':
        # Process the form data and extract the values
        city = request.POST.get('city')
        start_date = request.POST.get('start-date')
        end_date = request.POST.get('end-date')

        # Redirect to the package list page with the form values as query parameters
        return redirect(reverse('package:list_packages') + f'?price=&city={city}&start_date={start_date}&end_date={end_date}')
    
    package_data = []

    top_packages = Package.objects.annotate(num_clients=Count('clients')).order_by('-num_clients')[:6]
    for package in top_packages:
        attractions = package.attractions.all()
        tourist_spots = [attraction.touristspot for attraction in attractions]

        has_museum = any(tourist_spot for tourist_spot in tourist_spots if tourist_spot.type_tourist_spot == 0)
        has_park = any(tourist_spot for tourist_spot in tourist_spots if tourist_spot.type_tourist_spot == 2)
        has_concert_hall = any(tourist_spot for tourist_spot in tourist_spots if tourist_spot.type_tourist_spot == 3)
        has_church = any(tourist_spot for tourist_spot in tourist_spots if tourist_spot.type_tourist_spot == 1)

        package_info = {
            'package': package,
            'has_museum': has_museum,
            'has_park': has_park,
            'has_church': has_church,
            'has_concert_hall': has_concert_hall
        }

        package_data.append(package_info)


    cities = City.objects.all()
    return render(request, 'core/index.html', {
        'cities': cities,
        'package_data': package_data
    })

def vw_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            return HttpResponse('Error')
        
            
        
    
    return render(request, 'core/login.html')

def vw_register(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST['username']
        first_password = request.POST['first-password']
        second_password = request.POST['second-password']
        cpf = request.POST['CPF']

        if first_password != second_password:
            return HttpResponse('Senhas não equivalem')
        
        if len(cpf) != 11:
            return HttpResponse('CPF inválido')
        
        if len(username) < 4:
            return HttpResponse('Nome de usuário muito curto')
        
        usuario = User.objects.create_user(username=username, password=first_password)
        
        client = Client(user=usuario, cpf=cpf)
        client.save()

        login(request, usuario)
        return redirect('index')

    return render(request, 'core/register.html')

@login_required
def vw_logout(request):
    logout(request)
    return redirect('/')

def get_restaurants(request):
    city_id = request.GET.get('city_id')

    restaurants = Restaurant.objects.filter(city_id=city_id).values('id', 'name')

    return JsonResponse({'restaurants': list(restaurants)})


def get_hotels(request):
    city_id = request.GET.get('city_id')

    hotels = Hotel.objects.filter(city_id=city_id).values('id', 'name')

    return JsonResponse({'hotels': list(hotels)})

