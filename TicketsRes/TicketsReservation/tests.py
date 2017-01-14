from django.contrib.auth.models import User
from models import Sector, Event
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core.urlresolvers import resolve
from .forms import *


class TicketsReservationTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='admin', first_name='Jurand', last_name='zeSpychowa',
                                         email='jurand@o.pl')
        self.event1 = Event.objects.create(name='KinoBambino', address='test_adress', description='test_descr',
                                           website='web.web', user=self.user1, date='2017-01-10 17:16:35',
                                           img_url='http://www.zdjecfe.com/testfo.png')
        self.sector1 = Sector.objects.create(name='Sector1', max_column=5, max_row=10,
                                             event = self.event1, price = 21.37)
        self.ticket1 = Tickets.objects.create(event=self.event1, sector=self.sector1, column=2, row=3,
                                              guest_name='Andrew', guest_surname='Golara', guest_email='golara@o.pl')
        self.ticket2 = Tickets.objects.create(event=self.event1, sector=self.sector1, column=4, row=8,
                                              guest_name='Andrzej', guest_surname='Golota', guest_email='golota@o.pl')

    def test_ticket_data(self):
        self.assertEquals(self.ticket1.event, self.event1)
        self.assertEquals(self.ticket1.sector, self.sector1)
        self.assertEquals(self.ticket1.column, 2)
        self.assertEquals(self.ticket1.row, 3)
        self.assertEquals(self.ticket1.guest_surname, 'Golara')
        self.assertEquals(self.ticket1.guest_email, 'golara@o.pl')
        ticket_test2 = Tickets.objects.get(pk=2)
        self.assertNotEquals(ticket_test2.guest_name, 'Andrew')

    def test_model_relation(self):
        self.assertEquals(self.event1.tickets_set.count(), 2)
        self.assertEquals(self.sector1.tickets_set.count(), 2)

    def test_get_reservation_info(self):
        event_details = 'Event details:\n' + ' - name: ' + str(self.event1.name) + '\n - address: ' \
                        + str(self.event1.address) + '\n - description: ' + str(self.event1.description) \
                        + '\n - date: ' + str(self.event1.date)
        sector_details = '\n\nSector: ' + str(self.sector1.name)
        quest_details = '\n\nPersonal info:\n' + ' - name: ' + str(self.ticket2.guest_name) + ' ' \
                        + str(self.ticket2.guest_surname) + '\n - email: ' + str(self.ticket2.guest_email)
        self.assertEquals(self.ticket2.get_reservation_info(), event_details + sector_details + quest_details)

    def test_urls_names(self):
        url = reverse('about')
        self.assertEqual(url, '/about')
        url = reverse('contact')
        self.assertEqual(url, '/contact')
        url = reverse('user_home')
        self.assertEqual(url, '/user_home/')

    def test_url_connect_to_view(self):
        resolver = resolve('/')
        self.assertEqual(resolver.view_name, 'index')
        resolver = resolve('/about')
        self.assertEqual(resolver.view_name, 'about')
        resolver = resolve('/contact')
        self.assertEqual(resolver.view_name, 'contact')
        resolver = resolve('/user_home/')
        self.assertEqual(resolver.view_name, 'user_home')

    def test_TicketForm_valid(self):
        data = {'event': 1,
                'guest_name': "Andrzej",
                'guest_surname': "Golota",
                'guest_email': "golota@o.pl",
                'column': 4,
                'row': 8,
                'sector': 1}
        form = TicketForm(data=data, event_id=1)
        self.assertTrue(form.is_valid())

    def test_TicketForm_invalid(self):
            data = {'event': 2,
                    'guest_name': "Andrew",
                    'guest_surname': "Golara",
                    'guest_email': "golara@o.pl",
                    'column': 4,
                    'row': 8,
                    'sector': 1}
            form = TicketForm(data=data, event_id=3)
            self.assertFalse(form.is_valid())