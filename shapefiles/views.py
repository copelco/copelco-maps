from django.shortcuts import render
from django.views import generic

from shapefiles.models import Location, Place


class Home(generic.TemplateView):
    template_name = 'shapefiles/home.html'


class TypeList(generic.ListView):
    queryset = Location.objects.values_list('type', flat=True).distinct()
    template_name = 'shapefiles/list_types.html'
    context_object_name = 'types'


class LocationList(generic.ListView):
    template_name = 'shapefiles/list_locations.html'
    context_object_name = 'locations'

    def get_queryset(self):
        locations = Location.objects.filter(type=self.kwargs['location_type'])
        return locations.order_by('name')

    def get_context_data(self, **kwargs):
        data = super(LocationList, self).get_context_data(**kwargs)
        data['params'] = self.kwargs
        return data


class LocationView(generic.DetailView):

    def get_queryset(self):
        return Location.objects.filter(type=self.kwargs['location_type'])

    def get_context_data(self, **kwargs):
        data = super(LocationView, self).get_context_data(**kwargs)
        locations = Location.objects.filter(type=self.kwargs['location_type'])
        data['locations'] = locations.order_by('name')
        return data


def preview(request, location_type, location_id=None):
    locations = Location.objects.filter(type=location_type)
    if location_id:
        locations = locations.filter(pk=location_id)
    context = {'locations': locations}
    return render(request, 'preview.html', context)


class Places(generic.ListView):
    model = Place
    context_object_name = 'places'


class PlaceDetail(generic.DetailView):
    model = Place


home = Home.as_view()
list_places = Places.as_view()
view_place = PlaceDetail.as_view()
