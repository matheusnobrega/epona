from django.urls import path

from . import views

app_name = 'city'

urlpatterns = [
    path('', views.city_list, name='city_list'),
    path('<int:pk>/', views.city_detail, name="city_detail"),
    path('<int:pk>/delete/', views.city_delete, name="city_delete"),
    path('<int:pk>/update/', views.city_update, name="city_update"),
]