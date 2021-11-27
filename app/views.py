from django.shortcuts import redirect, render
from django.db import connections
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from .forms import *

# Create your views here.
class IndexView(generic.DetailView):
    INDEX = 'index.html'
    def get(self, request, *args, **kwargs):
        


        return render(request, self.INDEX, { 'form':geolocation()})

    def post(self, request):

        pass