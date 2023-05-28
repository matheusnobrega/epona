from django.contrib import admin

from .models import City, State

admin.site.register([State, City])
