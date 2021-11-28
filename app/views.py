from django.shortcuts import redirect, render
from django.db import connections
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from .forms import *
import requests
import googlemaps
import os
from dotenv import load_dotenv, find_dotenv
import gmaps
from ipywidgets.embed import embed_minimal_html
from pathlib import Path
load_dotenv(find_dotenv())
GMAPKEY = os.environ.get("GMAPKEY")


class IndexView(generic.DetailView):
    INDEX = 'index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.INDEX, { 'form':geolocation()})

    def post(self, request):
        form = geolocation(request.POST or None)
        if form.is_valid():
            geolocationinfo = form.cleaned_data
            ADDRESS = geolocationinfo["ADDRESS"]
            RADIUS = geolocationinfo["RADIUS"]
            gmaps = googlemaps.Client(key=GMAPKEY) 
            geocode_result = gmaps.geocode(geolocationinfo["ADDRESS"])
            lat, lng = get_location_from_geocode(geocode_result)
            filename = str(lat)+"&" + str(lng) + "&" + str(RADIUS) + '.html'
            my_file = Path("app/templates/"+filename)
            if  my_file.exists():
                return render(request, filename, { 'form':geolocation()})

            url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(lat) + "%2C" + str(lng) +"&radius=" + RADIUS + "&types=restaurant&key=" + GMAPKEY
            print(f'{url=}')
            resp = requests.get(url=url)
            respInput = resp.json()

            restaruants = cleanJson(respInput)

            heatmap(restaruants, lat, lng, filename)
            return render(request, filename)

# return format: <tuple> (49.191484, -122.8455741)s
def get_location_from_geocode(geo):
    if geo:
        lat = geo[0]["geometry"]["location"]["lat"]
        lng = geo[0]["geometry"]["location"]["lng"]
        return lat, lng
    else:
        return None

def cleanJson(originalJson):
    cleanedJson = []
    originalJson = originalJson["results"]
    for i in originalJson:
        for key, value in i.items():
            if key == "geometry":
                lat = value["location"]["lat"]
                lng = value["location"]["lng"]
                cleanedJson.append([lat, lng])
    return cleanedJson



def heatmap(restaruants, lat, lng, filename):
    gmaps.configure(api_key=GMAPKEY)
    input = restaruants
    fig = gmaps.figure(center=(lat, lng), zoom_level=13, layout={
            'width': '1920px',
            'height': '920px',
            'padding': '3px',
            'border': '1px solid black'})
    locations = input
    weights = [3] * len(input)
    heatmap = gmaps.heatmap_layer(locations, weights=weights)
    heatmap.max_intensity = 3.5
    heatmap.weights = [3] * len(input)
    heatmap.point_radius = 25
    fig.add_layer(heatmap)
    embed_minimal_html("./app/templates/"+filename, views=[fig])

