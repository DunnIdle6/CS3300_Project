from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from .models import *   #import all the models
from django.views import generic #so that we can inherit genric view stuff
from .forms import * #import all of our forms
from django.shortcuts import redirect
from datetime import datetime
from django.utils.safestring import mark_safe
from .utils import Calendar
from datetime import timedelta
import calendar
from django.contrib import messages
from django.contrib.auth.models import Group

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
        context['Concerts'] = Event.objects.all().filter(bands=self.get_object())
        return context

def BandCreate(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()

    return render(request, 'ensembled_app/band_create.html', {'form': form})

def BandUpdate(request, pk):
    band = Band.objects.get(pk=pk)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.pk)
    else:
        form = BandForm(instance=band)

    return render(request, 'ensembled_app/band_update.html', {'form': form})

def BandDelete(request, pk):
    band = Band.objects.get(pk=pk)

    if request.method == 'POST':
        band.delete()
        return redirect('bands')

    return render(request, 'ensembled_app/band_delete.html', {'band': band})

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
    
def MusicianCreate(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            musician = form.save()
            return redirect('musician-detail', musician.id)
    else:
        form = MusicianForm()

    return render(request, 'ensembled_app/musician_create.html', {'form': form})

def MusicianUpdate(request, pk):
    musician = Musician.objects.get(pk=pk)

    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('musician-detail', musician.pk)
    else:
        form = MusicianForm(instance=musician)

    return render(request, 'ensembled_app/musician_update.html', {'form': form})

def MusicianDelete(request, pk):
    musician = Musician.objects.get(pk=pk)

    if request.method == 'POST':
        musician.delete()
        return redirect('musicians')

    return render(request, 'ensembled_app/musician_delete.html', {'musician': musician})

class CalendarView(generic.ListView):
    model = Event
    template_name = 'ensembled_app/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('month', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        d = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime(year, month, day=1)
    return datetime.today()

class EventDetailView(generic.DetailView):
    model = Event
    #get all the members
    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['Bands'] = Band.objects.all().filter(Concerts=self.get_object())
        return context

def EventCreate(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return redirect('band-detail', event.id)
    else:
        form = EventForm()

    return render(request, 'ensembled_app/event_create.html', {'form': form})

def EventUpdate(request, pk):
    event = Event.objects.get(pk=pk)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event-detail', event.pk)
    else:
        form = EventForm(instance=event)

    return render(request, 'ensembled_app/event_update.html', {'form': form})

def EventDelete(request, pk):
    event = Event.objects.get(pk=pk)

    if request.method == 'POST':
        event.delete()
        return redirect('calendar')

    return render(request, 'ensembled_app/event_delete.html', {'band': event})

def registerPage(request):
    form = createUserForm()

    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='musician')
            user.groups.add(group)
            musician =  Musician.objects.create(user=user,)
            musician.save()

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
        
    context = {'form':form}
    return render(request, 'registration/register.html', context)



