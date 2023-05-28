from django.contrib import admin

from .models import Package, PackageAttraction

admin.site.register([Package, PackageAttraction])
