from django import forms   
from django.forms import DateInput
from .models import Band, Musician, Event

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        fields = '__all__'