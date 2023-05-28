import django_filters

from .models import Package, PackageAttraction

class PackageFilter(django_filters.FilterSet):
    price = django_filters.NumberFilter(lookup_expr='lte')
    start_date = django_filters.DateFilter(lookup_expr='gte')
    end_date = django_filters.DateFilter(lookup_expr='lte')
    class Meta:
        model = Package
        fields = [
            'start_date',
            'end_date',
            'price',
            'city',
        ]