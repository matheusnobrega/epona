from django.db import models

from city.models import City
from attraction.models import Attraction, Hotel
from client.models import Client

class Package(models.Model):
    price = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    city = models.ForeignKey(City, related_name='cities_package', on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, related_name='hotels_package', on_delete=models.CASCADE)
    attractions = models.ManyToManyField(Attraction, through='PackageAttraction')
    clients = models.ManyToManyField(Client, related_name="client_packages", blank=True)

class PackageAttraction(models.Model):
    package = models.ForeignKey(Package, related_name='packages', on_delete=models.CASCADE)
    attraction = models.ForeignKey(Attraction, related_name='attractions', on_delete=models.CASCADE)
    visitation_date = models.DateField()