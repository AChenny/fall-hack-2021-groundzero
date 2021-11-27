from django.shortcuts import redirect, render
from django.db import connections
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


# Create your views here.
class IndexView(generic.DetailView):
    INDEX = 'index.html'
    def get(self, request, *args, **kwargs):
        # fig = gmaps.figure()
        # # locations = [(49.23757, -122.99703), (49.22087, -123.00913)]
        # # locations = [(46.1, 5.2), (46.2, 5.3), (46.3, 5.4)]
        # # fig.add_layer(gmaps.heatmap_layer(locations))
        # # fig = gmaps.figure(center=(49, -122.0), zoom_level=8)

        # locations = [(46.1, 5.2), (46.2, 5.3), (46.3, 5.4)]
        # heatmap = gmaps.heatmap_layer(locations)

        # embed_minimal_html('export.html', views=[fig])


        return render(request, self.INDEX, {"hello": "Hello"})