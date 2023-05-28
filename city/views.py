from django.shortcuts import get_object_or_404, render, redirect
from .models import City, State
from django.http import HttpResponseRedirect
from django.urls import reverse


def city_list(request):
    cities = City.objects.order_by('state')

    return render(request, 'city/list.html', {
        'cities': cities,
    })

def city_detail(request, pk):
    city = get_object_or_404(City, pk=pk)

    return render(request, 'city/detail.html', {
        'city': city
    })

def city_delete(request, pk):
    city = get_object_or_404(City, pk=pk)

    if request.method == 'POST':
        city.delete()

        return redirect('index')
    
    return render(request, 'city/delete.html', {'city': city})

def city_update(request, pk):
    city = get_object_or_404(City, pk=pk)
    states = State.objects.all()

    if request.method == 'POST':
        city.name = request.POST.get('name')
        state_id = request.POST.get('state')
        city.state = State.objects.get(pk=state_id)
        city.population = request.POST.get('population')
        city.save()

        return HttpResponseRedirect(reverse('city:city_detail', args=[city.id]))


    return render(request, 'city/update.html', {
        'city': city,
        'states': states,
    })