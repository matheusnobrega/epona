from django.shortcuts import render, redirect
from city.models import City, State
from attraction.models import CategoryHotel, Park, Restaurant, Church, Hotel, Museum, CategoryRestaurant, ConcertHall, Founder
from package.models import Package
from django.http import HttpResponse
from django.conf import settings
import os


def create_city(request):
    if request.method == 'POST':
        name = request.POST['name']
        state_id = request.POST['state_id']
        population = request.POST['population']
        doc = request.FILES
        image = doc['image']

        state = State.objects.get(pk=state_id)
        if len(name) < 3:
            return HttpResponse('Error, name too short')
        
        path_image = 'images' + image.name
        complete_path = os.path.join(settings.MEDIA_ROOT, path_image)
        
        with open(complete_path, 'wb') as destino:
            for chunk in image.chunks():
                destino.write(chunk)
        
        new_city = City(name=name, state=state, population=population, image=path_image)
        new_city.save()

        return redirect('city:city_list')

    states = State.objects.all()

    return render(request, 'form/form_city.html', {
        'states': states,
    })

def create_hotel(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        city_id = request.POST['city_id']
        category_id = request.POST['category_id']
        rooms = request.POST['rooms']

        city = City.objects.get(pk=city_id)
        category = CategoryHotel.objects.get(pk=category_id)

        new_hotel = Hotel(city=city, address=address, type_attraction=0,
                          name=name, category=category, number_rooms=rooms)
        new_hotel.save()
        return redirect('attraction:hotel_detail', new_hotel.id)

    cities = City.objects.all()
    categories = CategoryHotel.objects.all()

    return render(request, 'form/form_hotel.html', {
        'cities': cities,
        'categories': categories,
    })

def create_restaurant(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        city_id = request.POST['city_id']
        category_id = request.POST['category_id']

        city = City.objects.get(pk=city_id)
        category = CategoryRestaurant.objects.get(pk=category_id)

        new_restaurant = Restaurant(city=city, address=address, 
                                    type_attraction=1,name=name, 
                                    category=category)
        new_restaurant.save()


    cities = City.objects.all()
    categories = CategoryRestaurant.objects.all()

    return render(request, 'form/form_restaurant.html', {
        'cities': cities,
        'categories': categories,
    })

def create_museum(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        city_id = request.POST['city_id']
        description = request.POST['description']
        rooms = request.POST['rooms']
        foundation_date = request.POST['foundation-date']

        city = City.objects.get(pk=city_id)


        new_museum = Museum(name=name, city=city, address=address, 
                            type_attraction=2, description=description,
                            type_tourist_spot=0, number_rooms=rooms,
                            foundation_date=foundation_date)
        new_museum.save()


    cities = City.objects.all()

    return render(request, 'form/form_museum.html', {
        'cities': cities,
    })

def create_church(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        city_id = request.POST['city_id']
        description = request.POST['description']
        construction_date = request.POST['construction-date']
        construction_style = request.POST['construction-style']

        city = City.objects.get(pk=city_id)


        new_church = Church(name=name, city=city, address=address, 
                            type_attraction=2, description=description,
                            type_tourist_spot=1,
                            construction_date=construction_date,
                            construction_style=construction_style)
        new_church.save()


    cities = City.objects.all()

    return render(request, 'form/form_church.html', {
        'cities': cities,
    })

def create_park(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        city_id = request.POST['city_id']
        description = request.POST['description']
        type = request.POST['type']

        city = City.objects.get(pk=city_id)

        new_park = Park(name=name, city=city, address=address, 
                        type_attraction=2, description=description,
                        type_tourist_spot=2, type=type)
        new_park.save()


    cities = City.objects.all()
    
    return render(request, 'form/form_park.html', {
        'cities': cities,
    })

def create_concert_hall(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        city_id = request.POST['city']
        description = request.POST['description']
        start_time = request.POST['start-time']
        closing_day =  request.POST['closing-day']
        restaurant_id = request.POST['restaurant']

        restaurant = None
        if restaurant_id != '':
            restaurant = Restaurant.objects.get(pk=restaurant_id)

        city = City.objects.get(pk=city_id)

        new_concert_hall = ConcertHall(name=name, city=city, address=address, 
                            type_attraction=2, description=description,
                            type_tourist_spot=3, start_time=start_time,
                            closing_day=closing_day, restaurant_hall=restaurant)
        new_concert_hall.save()


    cities = City.objects.all()
    
    return render(request, 'form/form_concert_hall.html', {
        'cities': cities,
    })



def create_package(request):
    if request.method == 'POST':
        price = request.POST['price']
        start_date = request.POST['start-date']
        end_date = request.POST['end-date']
        city_id = request.POST['city']
        hotel_id = request.POST['hotel']

        city = City.objects.get(pk=city_id)
        hotel = Hotel.objects.get(pk=hotel_id)

        new_package = Package(price=price, start_date=start_date, end_date=end_date,
                              city=city, hotel=hotel)
        new_package.save()

        return redirect('index')
    
    cities = City.objects.all()
    hotels = Hotel.objects.all()

    return render(request, 'form/create_package.html', {
        'cities': cities,
        'hotels': hotels,
    })


def create_founder(request):
    if request.method == 'POST':
        name = request.POST['name']
        birth_date = request.POST['birth-date']
        death_date = request.POST['death-date']
        nationality = request.POST['nationality']
        professional = request.POST['professional']

        new_founder = Founder(name=name, birth_date=birth_date, death_date=death_date,
                              nationality=nationality, professional=professional)
        new_founder.save()

    return render(request, 'form/form_founder.html')


def create(request):
    return render(request,'form/create.html')