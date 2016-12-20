from django.contrib.auth.models import User

from models import Event, Sector
from django.test import TestCase


class EventCreatorTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='admin', first_name='Jurand', last_name='zeSpychowa', email='jurand@o.pl')
        self.user2 = User.objects.create(username='mie1992', first_name='Zbyszko', last_name='zBogdanca', email='zbyszko@o.pl')
        self.event1 = Event.objects.create(name='KinoBambino', address='test_adress', description='test_descr',
                                           website='web.web', user=self.user1)
        self.event2 = Event.objects.create(name='Januszowo', address='test_adress1', description='testdscr',
                                           website='web.com', user=self.user1)
        self.event3 = Event.objects.create(name='Andrzejowo', address='test_adress12', description='testdscr1',
                                           website='web.com.pl', user=self.user2)
        self.sector1 = Sector.objects.create(name='Sektor1', max_column=5, max_row=10)

    def test_eventdata(self):
        self.assertEquals(self.event1.name, 'KinoBambino')
        self.assertEquals(self.event1.address, 'test_adress')
        self.assertEquals(self.event1.description, 'test_descr')
        self.assertEquals(self.event1.website, 'web.web')
        eventtest2 = Event.objects.get(pk=2)
        self.assertNotEquals(eventtest2.name, 'KinoBambino')

    def test_sectordata(self):
        self.assertEquals(self.sector1.name, 'Sektor1')
        self.assertEquals(self.sector1.max_column, 5)
        self.assertEquals(self.sector1.max_row, 10)

    def test_model_relation(self):
        self.assertEquals(self.user1.event_set.count(), 2)
        self.assertEquals(self.user2.event_set.count(), 1)
