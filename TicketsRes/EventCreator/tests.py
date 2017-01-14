from django.contrib.auth.models import User
from EventCreator.models import Event, Sector
from django.test import TestCase, RequestFactory, Client
from django.utils.datetime_safe import datetime
from django.core.urlresolvers import reverse, resolve
from .forms import *
from .views import *
from django.contrib.auth.models import User as Usr


class EventCreatorTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='admin', first_name='Jurand', last_name='zeSpychowa',
                                         email='jurand@o.pl')
        self.user2 = User.objects.create(username='mie1992', first_name='Zbyszko', last_name='zBogdanca',
                                         email='zbyszko@o.pl')
        self.event1 = Event.objects.create(name='KinoBambino', address='test_adress', description='test_descr',
                                           website='web.web', user=self.user1, date='2017-01-07 17:16:35',
                                           img_url='http://www.zdjecie.com/testfoto.png')
        self.event2 = Event.objects.create(name='Januszowo', address='test_adress1', description='testdscr',
                                           website='web.com', user=self.user1, date='2017-01-08 18:16:35',
                                           img_url='http://www.photo.com/test.jpg')
        self.event3 = Event.objects.create(name='Andrzejowo', address='test_adress12', description='testdscr1',
                                           website='web.com.pl', user=self.user2)
        self.sector1 = Sector.objects.create(name='Sektor1', max_column=5, max_row=10, event=self.event1, price=72.94)
        self.sector2 = Sector.objects.create(name='Sektor2', max_column=90, max_row=10, event=self.event2, price=2)
        self.factory = RequestFactory()
        self.user = Usr.objects.create_user(username='andrew', email='andrzej@andrzej.pl', password='supertajnehasuo')
        self.client = Client()

    def test_event_data(self):
        self.assertEquals(self.event1.name, 'KinoBambino')
        self.assertEquals(self.event1.address, 'test_adress')
        self.assertEquals(self.event1.description, 'test_descr')
        self.assertEquals(self.event1.website, 'web.web')
        self.assertEquals(self.event1.date, '2017-01-07 17:16:35')
        self.assertEquals(self.event1.img_url, 'http://www.zdjecie.com/testfoto.png')
        event_test2 = Event.objects.get(pk=2)
        self.assertNotEquals(event_test2.name, 'KinoBambino')
        event_test3 = Event.objects.get(pk=3)
        self.assertLessEqual(event_test3.date, datetime.now())

    def test_sectordata(self):
        self.assertEquals(self.sector1.name, 'Sektor1')
        self.assertEquals(self.sector1.max_column, 5)
        self.assertEquals(self.sector1.max_row, 10)
        self.assertEquals(self.sector1.price, 72.94)
        self.assertEquals(self.sector2.price, 2.00)

    def test_model_relation(self):
        self.assertEquals(self.user1.event_set.count(), 2)
        self.assertEquals(self.user2.event_set.count(), 1)

    def test_roles_str(self):
        event = Event.objects.get(pk=1)
        self.assertEqual(str(event), event.name)

    def test_sector_str(self):
        sector = Sector.objects.get(pk=1)
        self.assertEqual(str(sector), sector.name)

    def test_urls_names(self):
        url = reverse('add_event')
        self.assertEqual(url, '/add_event/')
        url = reverse('add_sector',kwargs={'event_id': 1})
        self.assertEqual(url, '/add_sector/1')
        url = reverse('confirm_cancel',kwargs={'event_id': 1})
        self.assertEqual(url, '/confirm_cancel/1')
        url = reverse('cancel_event',kwargs={'event_id': 1})
        self.assertEqual(url, '/cancel_event/1')
        url = reverse('edit_event',kwargs={'event_id': 1})
        self.assertEqual(url, '/edit_event/1')

    def test_url_connect_to_view(self):
        resolver = resolve('/add_event/')
        self.assertEqual(resolver.view_name, 'add_event')
        resolver = resolve('/add_sector/1')
        self.assertEqual(resolver.view_name, 'add_sector')
        resolver = resolve('/confirm_cancel/1')
        self.assertEqual(resolver.view_name, 'confirm_cancel')
        resolver = resolve('/cancel_event/1')
        self.assertEqual(resolver.view_name, 'cancel_event')
        resolver = resolve('/edit_event/1')
        self.assertEqual(resolver.view_name, 'edit_event')

    def test_login_view_loads(self):
        self.client.login(username='andrew', password='supertajnehasuo')
        response_edit_event = self.client.get('/edit_event/1')
        self.assertEqual(response_edit_event.status_code, 200)
        self.assertTemplateUsed(response_edit_event, 'edit_event.html')
        response_confirm_cancel = self.client.get('/confirm_cancel/1')
        self.assertEqual(response_confirm_cancel.status_code, 200)
        self.assertTemplateUsed(response_confirm_cancel, 'confirm_cancelation.html')
        response_cancel_event = self.client.get('/cancel_event/1')
        self.assertEqual(response_cancel_event.status_code, 200)
        self.assertTemplateUsed(response_cancel_event, 'user_home.html')
        response_add_sector = self.client.get('/add_sector/1')
        self.assertEqual(response_add_sector.status_code, 200)
        self.assertTemplateUsed(response_add_sector, 'add_sector.html')
        response_add_event = self.client.get('/add_event/')
        self.assertEqual(response_add_event.status_code, 200)
        self.assertTemplateUsed(response_add_event, 'add_event.html')

    def test_EventForm_valid(self):
        data = {'name': "KinoBambino",
                'address': "test_adress",
                'description': "test_descr",
                'website': "web.web",
                'img_url': "http://www.zdjecie.com/testfoto.png"}
        form = EventForm(data=data)
        self.assertTrue(form.is_valid())

    def test_SectorForm_valid(self):
        data = {'name': "Sektor1",
                'max_column': "5",
                'max_row': "10",
                'price': 21.30,
                'event': 1}
        form = SectorForm(data=data,event_id=1)
        self.assertTrue(form.is_valid())

    def test_add_event_view_post(self):
        data = {'name': "KinoBambin0",
                'address': "test_adress",
                'description': "test_descr",
                'website': "web.web",
                'img_url': "http://www.zdjecie.com/testfoto.png"}
        request = self.factory.post(reverse('add_event'), data)
        request.user = self.user
        response = add_event(request)
        self.assertEqual(response.status_code, 200)

    def test_add_event_view_get(self):
        request = self.factory.get(reverse('add_event'))
        request.user = self.user
        response = add_event(request)
        self.assertEqual(response.status_code, 200)

    def test_add_sector_view_post(self):
        data = {'name': "Sektor1",
                'max_column': "5",
                'max_row': "10",
                'price': 21.30,
                'event': 1}
        event_id = 1
        request = self.factory.post(reverse('add_sector', kwargs={'event_id': 1}), data)
        request.user = self.user
        response = add_sector(request, event_id)
        self.assertEqual(response.status_code, 200)

    def test_add_sector_view_get(self):
        event_id = 1
        request = self.factory.get(reverse('add_sector', kwargs={'event_id': 1}))
        request.user = self.user
        response = add_sector(request, event_id)
        self.assertEqual(response.status_code, 200)

    def test_edit_event(self):
        event_id = 1
        request = self.factory.get(reverse('edit_event', kwargs={'event_id': 1}))
        response = edit_event(request, event_id)
        self.assertEqual(response.status_code, 200)

    def test_cancel_event(self):
        event_id = 1
        request = self.factory.get(reverse('cancel_event', kwargs={'event_id': 1}))
        response = cancel_event(request, event_id)
        self.assertEqual(response.status_code, 200)

    def test_confirm_cancel_event(self):
        event_id = 1
        request = self.factory.get(reverse('confirm_cancel', kwargs={'event_id': 1}))
        response = confirm_cancel(request, event_id)
        self.assertEqual(response.status_code, 200)