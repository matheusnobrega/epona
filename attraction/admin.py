from django.contrib import admin

from .models import Attraction, Hotel, CategoryHotel, Room, Restaurant, ConcertHall, CategoryRestaurant, Museum, Founder, Park, Church

admin.site.register([Attraction, Hotel, CategoryHotel, 
                     Room, Restaurant, ConcertHall, CategoryRestaurant, 
                     Museum, Founder, Park, Church])
