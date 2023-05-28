from django.urls import path

from . import views

app_name = 'client'

urlpatterns = [
    path('<int:pk>', views.client_packages, name="client_packages"),
]