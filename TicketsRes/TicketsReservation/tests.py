from django.contrib.auth.models import User

from models import Sector, Event
from models import Tickets
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core.urlresolvers import resolve

class TicketsReservationTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='admin', first_name='Jurand', last_name='zeSpychowa', email='jurand@o.pl')
        self.event1 = Event.objects.create(name='KinoBambino', address='test_adress', description='test_descr',
                                           website='web.web', user=self.user1)
        self.sector1 = Sector.objects.create(name='Sektor1', max_column=5, max_row=10)
        self.ticket1 = Tickets.objects.create(event=self.event1, sector=self.sector1, column=2, row=3, price=12.01,
                                              guest_name='Andrew', guest_surname='Golara', guest_email='golara@o.pl')
        self.ticket2 = Tickets.objects.create(event=self.event1, sector=self.sector1, column=7, row=8, price=15.50,
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