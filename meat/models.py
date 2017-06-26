from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Animal(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class Part(models.Model):
    animal = models.ForeignKey(Animal, related_name='animal')
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class Cut(models.Model):
    cut = models.ForeignKey(Part, related_name='part')
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class AltPart(models.Model):
    part = models.ForeignKey(Part, related_name='alt')
    alt_name = models.CharField(max_length=256)
    def __str(self):
        return self.alt_name + " (" + str(self.cut.name)  + ")"


class AltCut(models.Model):
    cut = models.ForeignKey(Cut, related_name='alt')
    alt_name = models.CharField(max_length=256)
    def __str__(self):
        return self.alt_name + " (" + str(self.cut.name) + ")"

# class AustralianState(models.Model):
#     name = models.CharField(max_length=64)

class Supplier(models.Model):
    name = models.CharField(max_length=512, unique=True)
    logo = models.FileField(max_length=512, upload_to='images', blank=True)
    def __str__(self):
        return self.name


class Address(models.Model):
    STATE_CHOICES = (
        ("NSW", "New South Wales"),
        ("VIC", "Victoria"),
        ("QLD", "Queensland"),
        ("TAS", "Tasmania"),
        ("WA", "Western Australia"),
        ("NT", "Norther Territory"),
        ("ACT", "Australian Capital Territory"),
    )

    supplier = models.OneToOneField(Supplier, related_name='address', on_delete=models.CASCADE)
    address_line_one = models.CharField(max_length=512)
    address_line_two = models.CharField(max_length=512, blank=True)
    suburb = models.CharField(max_length=256)
    state = models.CharField(
        max_length=5,
        choices=STATE_CHOICES,
    )
    postcode = models.CharField(max_length=64)


class ContactDetails(models.Model):
    supplier = models.OneToOneField(Supplier, related_name='contact_details', on_delete=models.CASCADE)
    phone = models.CharField(max_length=64)
    email = models.CharField(max_length=512)
    latitude = models.DecimalField(decimal_places=5, max_digits=10)
    longitude = models.DecimalField(decimal_places=5, max_digits=10)


class Suburb(models.Model):
    name = models.CharField(max_length=512)
    postcode = models.CharField(max_length=5)
    state = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    latitude = models.DecimalField(decimal_places=5, max_digits=10)
    longitude = models.DecimalField(decimal_places=5, max_digits=10)
