from django.shortcuts import render, get_object_or_404, redirect

from .models import Hotel, Room, Restaurant

def hotel_list(request):
    hotels = Hotel.objects.order_by('city')

    return render(request, 'hotel/list.html', {
        'hotels': hotels
    })


def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    rooms = Room.objects.filter(hotel__id=pk)

    return render(request, 'hotel/detail.html', {
        'hotel': hotel,
        'rooms': rooms,
    })

def hotel_delete(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)

    if request.method == 'POST':
        hotel.delete()

        return redirect('index')
    
    return render(request, 'hotel/delete.html', {'hotel': hotel})


def add_room(request, pk):
    if request.method == 'POST':
        type = request.POST['type']
        price = request.POST['price']
        quantity = request.POST['quantity']
        
        hotel = Hotel.objects.get(pk=pk)
        new_room = Room(hotel=hotel, type=type, price=price, quantity=quantity)
        new_room.save()

        return redirect('attraction:hotel_detail', pk)
    
    return render(request, 'hotel/add_room.html', {'hotel_pk':pk})

def remove_room(request, pk, room_pk):
    room = get_object_or_404(Room, pk=room_pk)
    hotel = get_object_or_404(Hotel, pk=pk)

    if request.method == 'POST':
        room.delete()

        return redirect('attraction:hotel_detail', pk)


def add_restaurant(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)

    if request.method == 'POST':
        restaurant_id = request.POST['restaurant']

        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

        hotel.restaurant_hotel = restaurant
        hotel.save()

        return redirect('attraction:hotel_detail', pk)

    restaurants = Restaurant.objects.filter(city=hotel.city)

    return render(request, 'hotel/add_restaurant.html', {
        'restaurants': restaurants
    })

def remove_restaurant(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)

    if request.method == 'POST':
        hotel.restaurant_hotel = None
        hotel.save()

        return redirect('attraction:hotel_detail', pk)
