from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=32)
    role = models.ForeignKey(Role)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    date = models.DateField()
    description = models.CharField(max_length=200)
    website = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField(max_length=32)
    max_column = models.IntegerField()
    max_row = models.IntegerField()

    def __str__(self):
        return self.name


class Tickets(models.Model):
    event = models.ForeignKey(Event)
    sector = models.ForeignKey(Sector)
    column = models.IntegerField()
    row = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    guest_name = models.CharField(max_length=32)
    guest_surname = models.CharField(max_length=32)
    guest_email = models.CharField(max_length=32)

    def __str__(self):
        return self.name
