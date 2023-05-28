from django.urls import path

from . import views

app_name = 'attraction'

urlpatterns = [
    path('hotels/', views.hotel_list, name="hotel_list"),
    path('hotel/<int:pk>/', views.hotel_detail, name="hotel_detail"),
    path('hotel/<int:pk>/delete', views.hotel_delete, name="hotel_delete"),
    path('hotel/<int:pk>/add_room/', views.add_room, name="add_room"),
    path('hotel/<int:pk>/remove_room/<int:room_pk>/', views.remove_room, name="remove_room"),
    path('hotel/<int:pk>/add_restaurant/', views.add_restaurant, name="add_restaurant"),
    path('hotel/<int:pk>/remove_restaurant/', views.remove_restaurant, name="remove_restaurant"),
]