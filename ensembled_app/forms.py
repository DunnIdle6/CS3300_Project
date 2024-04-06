from django import forms   
from .models import Band, Musician

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'