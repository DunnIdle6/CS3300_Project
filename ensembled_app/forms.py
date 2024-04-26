from django import forms   
from django.forms import DateInput
from .models import Band, Musician, Event
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

