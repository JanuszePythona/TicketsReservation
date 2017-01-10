from __future__ import unicode_literals
from django.db import models

from EventCreator.models import Sector, Event


class Tickets(models.Model):
    event = models.ForeignKey(Event)
    sector = models.ForeignKey(Sector)
    column = models.IntegerField()
    row = models.IntegerField()
    guest_name = models.CharField(max_length=32)
    guest_surname = models.CharField(max_length=32)
    guest_email = models.CharField(max_length=32)
