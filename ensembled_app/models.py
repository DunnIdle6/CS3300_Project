from django.db import models
from django.urls import reverse

# Create your models here.
class Musician(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    about = models.TextField(blank=True)
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
        ("Alternative","Alternative"),
        ("Blues","Blues"),
        ("Classical","Classical"),
        ("Concert Band","Concert Band"),
        ("Country","Country"),
        ("Electronic","Electronic"),
        ("Folk","Folk"),
        ("Hip Hop","Hip Hop"),
        ("Jazz","Jazz"),
        ("Latin","Latin"),
        ("Metal","Metal"),
        ("Orchestral","Orchestral"),
        ("Pop","Pop"),
        ("R&B","R&B"),
        ("Rock","Rock"),
        ("World","World"),
        ("Other", "Other")
    )
    genre = models.CharField(max_length=100, choices=GENRES)
    about = models.TextField(blank=True)
    isOpen = models.BooleanField(default=True)
    members = models.ManyToManyField(Musician, related_name="Bands", blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("band-detail", kwargs={"pk": self.pk})
