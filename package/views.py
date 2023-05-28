from django.shortcuts import render, get_object_or_404, redirect
from city.models import City
from attraction.models import Hotel, Museum, Park, ConcertHall, Church, Attraction
from .models import Package, PackageAttraction
from client.models import Client
from .filters import PackageFilter
from django.http import HttpResponseRedirect
from django.urls import reverse
import json

def list_packages(request):
    context = {}
    package_data = []

    filtered_packages = PackageFilter(
        request.GET,
        queryset=Package.objects.all()
    )

    context['filtered_packages'] =  filtered_packages

    for package in filtered_packages.qs:
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
        

    return render(request, 'package/list.html', {
        'package_data': package_data,
        'filtered_packages': filtered_packages})


def package_detail(request, pk):
    package = get_object_or_404(Package, pk=pk)
    package_attractions = PackageAttraction.objects.filter(package=package)
    client = None
    has_bought = False
    
    if request.user.is_authenticated:
        client = request.user.client
        has_bought = client.client_packages.filter(pk=pk).exists()


    return render(request, 'package/detail.html', {
        'package': package,
        'package_attractions': package_attractions,
        'client': client,
        'has_bought': has_bought,
    })

def package_delete(request, pk):
    package = get_object_or_404(Package, pk=pk)

    if request.method == 'POST':
        package.delete()

        return redirect('index')
    
    return render(request, 'package/delete.html', {'package': package})

def package_update(request, pk):
    package = get_object_or_404(Package, pk=pk)
    cities = City.objects.all()

    if request.method == 'POST':
        package.price = request.POST.get('price')
        package.start_date = request.POST.get('start-date')
        package.end_date = request.POST.get('start-date')
        city_id = request.POST.get('city')
        package.city = City.objects.get(pk=city_id)
        hotel_id = request.POST.get('hotel')
        package.hotel = Hotel.objects.get(pk=hotel_id)
        package.save()

        return HttpResponseRedirect(reverse('package:package_detail', args=[package.id]))

    return render(request, 'package/update.html', {
        'package': package,
        'cities': cities
    })

def add_attraction(request, package_pk):
    package = get_object_or_404(Package, pk=package_pk)

    if request.method == 'POST':
        attraction_id = request.POST.get('atracao')
        visitation_date = request.POST.get('visitation-date')

        attraction = get_object_or_404(Attraction, pk=attraction_id)

        new_package_attraction = PackageAttraction(package=package, attraction=attraction,
                                                   visitation_date=visitation_date)
        new_package_attraction.save()

        return redirect('package:package_detail', package_pk)


    city = package.city
    museums = Museum.objects.filter(city=city)
    parks = Park.objects.filter(city=city)
    concert_halls = ConcertHall.objects.filter(city=city)
    churches = Church.objects.filter(city=city)

    return render(request, 'package_attraction/add_attraction.html', {
        'museums_json': json.dumps(list(museums.values('id', 'name'))),
        'churches_json': json.dumps(list(churches.values('id', 'name'))),
        'parks_json': json.dumps(list(parks.values('id', 'name'))),
        'concert_halls_json': json.dumps(list(concert_halls.values('id', 'name'))),
        'package': package,
    })

def remove_attraction(request, pk, pack_attr_pk):
    package_attraction = get_object_or_404(PackageAttraction, pk=pack_attr_pk)

    if request.method == 'POST':
        package_attraction.delete()

        return redirect('package:package_detail', pk)

def buy_package(request, pk):
    if request.method == 'POST':
        package = get_object_or_404(Package, pk=pk)
        client = get_object_or_404(Client, user_id=request.user.id)

        package.clients.add(client)

        return redirect('client:client_packages', request.user.id)
    else: 
        return redirect('package:package_detail', pk)

def sell_package(request, pk):
    if request.method == 'POST':
        package = get_object_or_404(Package, pk=pk)
        user = request.user
        client = get_object_or_404(Client, user=user)

        package.clients.remove(client)
        
        return redirect('client:client_packages', request.user.id)
    else: 
        return redirect('package:package_detail', pk)


def filter_packages(request):
    if request.method== 'POST':
        city_id = request.POST['city']
        start_date = request.POST['start-date']
        end_date = request.POST['end-date']

        city = City.objects.get(pk=city_id)        
        packages = Package.objects.filter(city=city, start_date=start_date,
                                          end_date=end_date)
        
        return render(request, 'packages.html', {'packages': packages})

# def hotel_detail(request, pk):
#     hotel = get_object_or_404(Hotel, pk=pk)
#     rooms = Room.objects.filter(hotel__id=pk)

#     return render(request, 'hotel/detail.html', {
#         'hotel': hotel,
#         'rooms': rooms,
#     })

        
    #     hotel = Hotel.objects.get(pk=pk)
    #     new_room = Room(hotel=hotel, type=type, price=price, quantity=quantity)
    #     new_room.save()

    #     return redirect('attraction:hotel_detail', pk)
    
    # return render(request, 'hotel/add_room.html', {'hotel_pk':pk})
