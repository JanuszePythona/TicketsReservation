from django.contrib.auth.models import User
from models import Event, Sector
from django.test import TestCase
from django.utils.datetime_safe import datetime


class EventCreatorTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='admin', first_name='Jurand', last_name='zeSpychowa', email='jurand@o.pl')
        self.user2 = User.objects.create(username='mie1992', first_name='Zbyszko', last_name='zBogdanca', email='zbyszko@o.pl')
        self.event1 = Event.objects.create(name='KinoBambino', address='test_adress', description='test_descr',
                                           website='web.web', user=self.user1,date='2017-01-07 17:16:35')
        self.event2 = Event.objects.create(name='Januszowo', address='test_adress1', description='testdscr',
                                           website='web.com', user=self.user1, date='2017-01-08 18:16:35')
        self.event3 = Event.objects.create(name='Andrzejowo', address='test_adress12', description='testdscr1',
                                           website='web.com.pl', user=self.user2)
        self.sector1 = Sector.objects.create(name='Sektor1', max_column=5, max_row=10)

    def test_event_data(self):
        self.assertEquals(self.event1.name, 'KinoBambino')
        self.assertEquals(self.event1.address, 'test_adress')
        self.assertEquals(self.event1.description, 'test_descr')
        self.assertEquals(self.event1.website, 'web.web')
        self.assertEquals(self.event1.date, '2017-01-07 17:16:35')
        event_test2 = Event.objects.get(pk=2)
        self.assertNotEquals(event_test2.name, 'KinoBambino')
        event_test3 = Event.objects.get(pk=3)
        self.assertNotEquals(event_test3.date, datetime.now())

    def test_sectordata(self):
        self.assertEquals(self.sector1.name, 'Sektor1')
        self.assertEquals(self.sector1.max_column, 5)
        self.assertEquals(self.sector1.max_row, 10)

    def test_model_relation(self):
        self.assertEquals(self.user1.event_set.count(), 2)
        self.assertEquals(self.user2.event_set.count(), 1)

    def test_roles_str(self):
        event = Event.objects.get(pk=1)
        self.assertEqual(str(event), event.name)

    def test_sector_str(self):
        sector = Sector.objects.get(pk=1)
        self.assertEqual(str(sector), sector.name)