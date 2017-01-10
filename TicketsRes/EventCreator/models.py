from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils.datetime_safe import datetime


class Event(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=10000)
    website = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    date = models.DateTimeField(default=datetime.now, blank=True)
    img_url = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField(max_length=32)
    max_column = models.IntegerField()
    max_row = models.IntegerField()
    event = models.ForeignKey(Event)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
