from django.db import models
from city.models import City 

class Attraction(models.Model):
    city = models.ForeignKey(City, related_name='cities', on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    type_attraction = models.IntegerField()


class CategoryRestaurant(models.Model):
    description = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.description
    
class Restaurant(Attraction):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(CategoryRestaurant, related_name='categories_restaurant', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class CategoryHotel(models.Model):
    description = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.description

class Hotel(Attraction):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(CategoryHotel, related_name='categories_hotel', on_delete=models.CASCADE)
    number_rooms = models.IntegerField()
    restaurant_hotel = models.OneToOneField(Restaurant, related_name='restaurants_hotel', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='hotels', on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.type

class TouristSpot(Attraction):
    description = models.CharField(max_length=300)
    type_tourist_spot = models.IntegerField()
    name = models.CharField(max_length=100)

class ConcertHall(TouristSpot):
    start_time = models.TimeField()
    closing_day = models.CharField(max_length=15)
    restaurant_hall = models.OneToOneField(Restaurant, related_name='restaurants_hall', null=True, blank=True, on_delete=models.SET_NULL)

class Church(TouristSpot):
    construction_date = models.DateField()
    construction_style = models.CharField(max_length=50)

class Park(TouristSpot):
    type = models.CharField(max_length=15)

class Museum(TouristSpot):
    number_rooms = models.IntegerField()
    foundation_date = models.DateField()

class Founder(models.Model):
    name = models.CharField(max_length=30)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=15)
    professional_activity = models.CharField(max_length=15)
    museums = models.ManyToManyField(Museum)

