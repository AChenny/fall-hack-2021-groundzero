from django.shortcuts import redirect, render
from django.db import connections
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


# Create your views here.
class IndexView(generic.DetailView):
    INDEX = 'index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.INDEX)