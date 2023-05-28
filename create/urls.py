from django.contrib.admin.views.decorators import user_passes_test
from django.urls import path

from . import views

app_name = 'create'

def is_superuser(user):
    return user.is_superuser

urlpatterns = [
    path('city/', views.create_city, name="create_city"),
    path('hotel/', views.create_hotel, name="create_hotel"),
    path('restaurant/', views.create_restaurant, name="create_restaurant"),
    path('museum/', views.create_museum, name="create_museum"),
    path('church/', views.create_church, name="create_church"),
    path('park/', views.create_park, name="create_park"),
    path('concerthall/', views.create_concert_hall, name="create_concert_hall"),
    path('package/', views.create_package, name="create_package"),
    path('founder/', views.create_founder, name="create_founder"),
    path('', user_passes_test(is_superuser) (views.create), name="create")
]