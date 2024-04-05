from django.db import models
from django.urls import reverse

# Create your models here.
class Musician(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    #bands
    instruments = models.CharField(max_length=100)
    isLooking = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("musician-detail", kwargs={"pk": self.pk})
    
class Band(models.Model):
    name = models.CharField(max_length=100)
    GENRES = (
        ("ALT","Alternative"),
        ("BLU","Blues"),
        ("CLA","Classical"),
        ("CON","Concert Band"),
        ("CNT","Country"),
        ("ELE","Electronic"),
        ("FLK","Folk"),
        ("HPH","Hip Hop"),
        ("JAZ","Jazz"),
        ("LTN","Latin"),
        ("MET","Metal"),
        ("ORC","Orchestral"),
        ("POP","Pop"),
        ("RAB","R&B"),
        ("RCK","Rock"),
        ("WLD","World")
    )
    genre = models.CharField(max_length=100, choices=GENRES)
    isOpen = models.BooleanField(default=True)
    members = models.ManyToManyField(Musician, related_name="Bands")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("band-detail", kwargs={"pk": self.pk})
