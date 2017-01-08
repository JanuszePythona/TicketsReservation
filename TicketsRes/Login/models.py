from __future__ import unicode_literals
from django.db import models


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
