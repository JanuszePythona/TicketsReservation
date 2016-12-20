from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    description = models.CharField(max_length=200)
    website = models.CharField(max_length=32)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField(max_length=32)
    max_column = models.IntegerField()
    max_row = models.IntegerField()

    def __str__(self):
        return self.name
