from __future__ import unicode_literals

from django.db import models

from EventCreator.models import Sector, Event
from Login.models import User


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
