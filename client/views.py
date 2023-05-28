from django.shortcuts import render
from .models import Client
from django.db import connection

def client_packages(request, pk):
 client = Client.objects.get(user_id=pk)
 packages = client.client_packages.all()
 package_data = []

 with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM getTotalCost(%s)", [client.id])
        total_cost = cursor.fetchone()[0]

 for package in packages:
        attractions = package.attractions.all()
        tourist_spots = [attraction.touristspot for attraction in attractions]

        has_museum = any(tourist_spot.museum for tourist_spot in tourist_spots if tourist_spot.type_tourist_spot == 0)
        has_park = any(tourist_spot.park for tourist_spot in tourist_spots if tourist_spot.type_tourist_spot == 2)
        has_concert_hall = any(tourist_spot.concerthall for tourist_spot in tourist_spots if tourist_spot.type_tourist_spot == 3)
        has_church = any(tourist_spot.church for tourist_spot in tourist_spots if tourist_spot.type_tourist_spot == 1)

        package_info = {
            'package': package,
            'has_museum': has_museum,
            'has_park': has_park,
            'has_church': has_church,
            'has_concert_hall': has_concert_hall
        }

        package_data.append(package_info)

 return render(request, 'client/packages.html', {
  'client': client,
  'packages': packages,
  'package_data': package_data,
  'total_cost': total_cost,
 })
