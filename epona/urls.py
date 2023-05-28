from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core.views import index, get_hotels, vw_login, vw_register, vw_logout, get_restaurants
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('attractions/', include('attraction.urls')),
    path('cities/', include('city.urls')),
    path('packages/', include('package.urls')),
    path('create/', include('create.urls')),
    path('client/', include('client.urls')),
    path('login/', vw_login, name='vw_login'),
    path('register/', vw_register, name='vw_register'),
    path('logout/', vw_logout, name='vw_logout'),
    path('ajax/hoteis/', get_hotels, name='get_hotels'),
    path('ajax/restaurants/', get_restaurants, name='get_restaurants'),
]

urlpatterns +=  static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)