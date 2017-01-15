from __future__ import unicode_literals

import StringIO
import qrcode

from EventCreator.models import Sector, Event
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse
from django.db import models


class Tickets(models.Model):
    event = models.ForeignKey(Event)
    sector = models.ForeignKey(Sector)
    column = models.IntegerField(validators=[MinValueValidator(0)])
    row = models.IntegerField(validators=[MinValueValidator(0)])
    guest_name = models.CharField(max_length=32)
    guest_surname = models.CharField(max_length=32)
    guest_email = models.CharField(max_length=32)
    qrcode = models.ImageField(upload_to='qrcode', blank=True, null=True)

    def get_reservation_info(self):
        event_details = 'Event details:\n' + ' - name: ' + str(self.event.name) + '\n - address: ' \
                        + str(self.event.address) + '\n - description: ' + str(self.event.description) \
                        + '\n - date: ' + str(self.event.date)
        sector_details = '\n\nSector: ' + str(self.sector.name)
        quest_details = '\n\nPersonal info:\n' + ' - name: ' + str(self.guest_name) + ' ' + str(self.guest_surname) \
                        + '\n - email: ' + str(self.guest_email)
        return event_details + sector_details + quest_details

    def generate_qrcode(self): # pragma: no cover
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=0,
        )
        qr.add_data('www.google.com')
        qr.make(fit=True)
        img = qr.make_image()
        buffer = StringIO.StringIO()
        img.save(buffer)
        filename = 'events-%s.png' % (self.id)
        filebuffer = InMemoryUploadedFile(buffer, None, filename, 'image/png', buffer.len, None)
        self.qrcode.save(filename, filebuffer)