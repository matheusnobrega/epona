from django.urls import path

from . import views

app_name = 'package'

urlpatterns = [
    path('', views.filter_packages, name="filter_packages"),
    path('all_packages', views.list_packages, name='list_packages'),
    path('<int:pk>/', views.package_detail, name="package_detail"),
    path('<int:pk>/delete', views.package_delete, name="package_delete"),
    path('<int:pk>/update', views.package_update, name="package_update"),
    path('<int:pk>/buy', views.buy_package, name="buy_package"),
    path('<int:pk>/sell', views.sell_package, name="sell_package"),
    path('<int:package_pk>/add_attraction', views.add_attraction, name="add_attraction"),
    path('<int:pk>/remove_attraction/<int:pack_attr_pk>', views.remove_attraction, name="remove_attraction"),
]