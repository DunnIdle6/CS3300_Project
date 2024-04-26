from django.test import TestCase
from .models import * #import all the models for testing
from .forms import *

#2test models, 2test forms, 2test views
#checkout https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing

# Create your tests here.
class MusicianModelTest(TestCase):
    def setUpTestData():
        Musician.objects.create(name = 'mr. test', instruments = 'instrument')
    
    def test_name_label(self):
        musician = Musician.objects.get(id=1)
        field_label = musician._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_instruments_label(self):
        musician = Musician.objects.get(id=1)
        field_label = musician._meta.get_field('instruments').verbose_name
        self.assertEquals(field_label, 'instruments')

    def test_isLooking_default(self):
        musician = Musician.objects.get(id=1)
        self.assertTrue(musician.isLooking)

    def test_get_absolute_url(self):
        musician = Musician.objects.get(id=1)
        self.assertEquals(musician.get_absolute_url(), '/musicians/1')

class BandModelTest(TestCase):
    def setUpTestData():
        Band.objects.create(name='TestBand', genre='Rock')

    def test_name_label(self):
        band = Band.objects.get(id=1)
        field_label = band._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_genre_label(self):
        band = Band.objects.get(id=1)
        field_label = band._meta.get_field('genre').verbose_name
        self.assertEquals(field_label, 'genre')

    def test_isOpen_default(self):
        band = Band.objects.get(id=1)
        self.assertTrue(band.isOpen)

    def test_members_relation(self):
        musician = Musician.objects.create(name='mr. test', instruments='instrument')
        band = Band.objects.get(id=1)
        band.members.add(musician)
        self.assertIn(musician, band.members.all())

    def test_get_absolute_url(self):
        band = Band.objects.get(id=1)
        self.assertEquals(band.get_absolute_url(), '/bands/1')

class MusicianFormTest(TestCase):
    def test_musician_form_valid_data(self):
        form = MusicianForm(data={
            'name': 'a name',
            'email': 'an email',
            'about': 'a brief sentence',
            'instruments': 'instrument',
            'isLooking': True
        })
        self.assertTrue(form.is_valid())

    def test_musician_form_blank_data(self):
        form = MusicianForm(data={})
        self.assertFalse(form.is_valid())

class BandFormTest(TestCase):
    def test_band_form_valid_data(self):
        form = BandForm(data={
            'name': 'band name',
            'genre': 'Rock',
            'about': 'sentencey.',
            'isOpen': True,
        })
        self.assertTrue(form.is_valid())

    def test_band_form_blank_data(self):
        form = BandForm(data={})
        self.assertFalse(form.is_valid())

        