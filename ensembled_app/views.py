from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from .models import *   #import all the models
from django.views import generic #so that we can inherit genric view stuff
from .forms import * #import all of our forms
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'ensembled_app/index.html')

class BandsListView(generic.ListView):
    model = Band
    context_object_name = 'Band_list'

class BandDetailView(generic.DetailView):
    model = Band
    #get all the members
    def get_context_data(self, **kwargs):
        context = super(BandDetailView, self).get_context_data(**kwargs)
        context['Members'] = Musician.objects.all().filter(Bands=self.get_object())
        return context
    
class MusicianListView(generic.ListView):
    model = Musician
    context_object_name = 'Musician_list'

class MusicianDetailView(generic.DetailView):
    model = Musician
    context_object_name = 'Musician'
    #get all their joined bands
    def get_context_data(self, **kwargs):
        context = super(MusicianDetailView, self).get_context_data(**kwargs)
        context['Bands'] = Band.objects.all().filter(members=self.get_object())
        return context