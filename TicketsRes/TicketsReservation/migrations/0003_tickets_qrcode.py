# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-12 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicketsReservation', '0002_remove_tickets_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='qrcode',
            field=models.ImageField(blank=True, null=True, upload_to='qrcode'),
        ),
    ]
