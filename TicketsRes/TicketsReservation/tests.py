from django.test import TestCase
from TicketsReservation.models import Tickets
from EventCreator.models import Sector, Event
from Login.models import User,Role

# Create your tests here.
class TicketsReservationTestCase(TestCase):
    def setUp(self):
        self.role1 = Role.objects.create(name='User')
        self.user1 = User.objects.create(name='Jurand', surname='zeSpychowa', email='jurand@o.pl',phone_number='12343', role=self.role1)
        self.event1 = Event.objects.create(name='KinoBambino', address='test_adress', description='test_descr', website='web.web', user=self.user1)
        self.sector1 = Sector.objects.create(name='Sektor1', max_column=5, max_row=10)
        self.ticket1 = Tickets.objects.create(event=self.event1, sector=self.sector1, column=2, row=3, price=12.01, guest_name='Andrew', guest_surname='Golara', guest_email = 'golara@o.pl')
        self.ticket2 = Tickets.objects.create(event=self.event1, sector=self.sector1, column=7, row=8, price=15.50, guest_name='Andrzej', guest_surname='Golota', guest_email='golota@o.pl')

    def test_ticketdata(self):
        self.assertEquals(self.ticket1.event, self.event1)
        self.assertEquals(self.ticket1.sector, self.sector1)
        self.assertEquals(self.ticket1.column, 2)
        self.assertEquals(self.ticket1.row, 3)
        self.assertEquals(self.ticket1.price, 12.01)
        self.assertEquals(self.ticket1.guest_name, 'Andrew')
        self.assertEquals(self.ticket1.guest_surname, 'Golara')
        self.assertEquals(self.ticket1.guest_email, 'golara@o.pl')

        tickettest2 = Tickets.objects.get(pk=2)
        self.assertNotEquals(tickettest2.guest_name, 'Andrew')

    def test_model_relatio(self):
        self.assertEquals(self.event1.tickets_set.count(), 2)
        self.assertEquals(self.sector1.tickets_set.count(), 2)