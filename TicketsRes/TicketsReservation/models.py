from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=32)
    role = models.OneToOneField(Role)

    def __str__(self):
        return self.name
