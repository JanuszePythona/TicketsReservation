# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-10 22:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TicketsReservation', '0003_event_sector_tickets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='user',
        ),
        migrations.AlterField(
            model_name='tickets',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventCreator.Event'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventCreator.Sector'),
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Sector',
        ),
    ]
