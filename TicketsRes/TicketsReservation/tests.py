from models import Sector, Event
from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse, resolve
from .forms import *
from .views import *
from django.contrib.auth.models import User as Usr


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
        self.factory = RequestFactory()
        self.user = Usr.objects.create_user(username='andrew', email='andrzej@andrzej.pl', password='supertajnehasuo')

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
        url = reverse('view_event', kwargs={'event_id': 1})
        self.assertEqual(url, '/event/1')
        url = reverse('place_reservation', kwargs={'event_id': 1})
        self.assertEqual(url, '/place_reservation/1')

    def test_url_connect_to_view(self):
        resolver = resolve('/')
        self.assertEqual(resolver.view_name, 'index')
        resolver = resolve('/about')
        self.assertEqual(resolver.view_name, 'about')
        resolver = resolve('/contact')
        self.assertEqual(resolver.view_name, 'contact')
        resolver = resolve('/user_home/')
        self.assertEqual(resolver.view_name, 'user_home')
        resolver = resolve('/event/1')
        self.assertEqual(resolver.view_name, 'view_event')
        resolver = resolve('/place_reservation/1')
        self.assertEqual(resolver.view_name, 'place_reservation')

    def test_login_view_loads(self):
        self.client.login(username='andrew', password='supertajnehasuo')
        response_index = self.client.get('/')
        self.assertEqual(response_index.status_code, 200)
        self.assertTemplateUsed(response_index, 'index.html')
        response_about = self.client.get('/about')
        self.assertEqual(response_about.status_code, 200)
        self.assertTemplateUsed(response_about, 'about.html')
        response_contact = self.client.get('/contact')
        self.assertEqual(response_contact.status_code, 200)
        self.assertTemplateUsed(response_contact, 'contact.html')
        response_user_home = self.client.get('/user_home/')
        self.assertEqual(response_user_home.status_code, 200)
        self.assertTemplateUsed(response_user_home, 'user_home.html')
        response_view_event = self.client.get('/event/1')
        self.assertEqual(response_view_event.status_code, 200)
        self.assertTemplateUsed(response_view_event, 'event.html')
        response_place_reservation = self.client.get('/place_reservation/1')
        self.assertEqual(response_place_reservation.status_code, 200)
        self.assertTemplateUsed(response_place_reservation, 'place_reservation.html')

    def test_TicketForm_valid(self):
        data = {'event': 1,
                'guest_name': "Andrzej",
                'guest_surname': "Dooda",
                'guest_email': "golota@o.pl",
                'column': 7,
                'row': 8,
                'sector': 1}
        form = TicketForm(data=data, event_id=1)
        self.assertTrue(form.is_valid())

    def test_index(self):
        request = self.factory.get(reverse('index'))
        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        request = self.factory.get(reverse('about'))
        response = about(request)
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        request = self.factory.get(reverse('contact'))
        response = contact(request)
        self.assertEqual(response.status_code, 200)

    def test_view_event(self):
        event_id = 1
        request = self.factory.get(reverse('view_event',kwargs={'event_id': 1}))
        response = view_event(request, event_id)
        self.assertEqual(response.status_code, 200)

    def test_view_user_home(self):
        request = self.factory.get(reverse('user_home'))
        request.user = self.user
        response = user_home(request)
        self.assertEqual(response.status_code, 200)

    def test_place_reservation_post(self):
        data = {'event': 1,
                'guest_name': "Andrew",
                'guest_surname': "Golara",
                'guest_email': "golara@o.pl",
                'column': 7,
                'row': 5,
                'sector': 1}
        request = self.factory.post(reverse('place_reservation', kwargs={'event_id': 1}), data)
        request.user = self.user
        response = place_reservation(request, 1)
        self.assertEqual(response.status_code, 200)

    def test_place_reservation_get(self):
        request = self.factory.get(reverse('place_reservation', kwargs={'event_id': 2}))
        response = place_reservation(request, 2)
        self.assertEqual(response.status_code, 200)