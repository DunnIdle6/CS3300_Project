from django.test import TestCase
from .models import * #import all the models for testing

#2test models, 2test forms, 2test views

# Create your tests here.
class TestBand(TestCase):
    def setUp(self):
        Band.objects.create(name="band1", genre="Jazz", about="ABOUT ME BAND", isOpen="False")

    def testBandSTR(self):
        band = Band.objects.get(name="band1")
        self.assertEqual(band.__str__(), "band1")

    def testBandName(self):
        band = Band.objects.get(name="band1")
        self.assertEqual(band.name, "band1")    