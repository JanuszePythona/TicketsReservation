from django.test import TestCase

# Create your tests here.
from Login.models import User,Role

# Create your tests here.
class LoginTestCase(TestCase):
    def setUp(self):
        self.role1 = Role.objects.create(name='User')
        self.role2 = Role.objects.create(name='Admin')
        self.user1 = User.objects.create(name='Jurand', surname='zeSpychowa', email='jurand@o.pl',phone_number='12343', role=self.role1)
        self.user2 = User.objects.create(name='Zbyszko', surname='zBogdanca', email='zbyszko@o.pl', phone_number='1233', role=self.role1)

    def test_userdata(self):
        self.assertEquals(self.user1.name, 'Jurand')
        self.assertEquals(self.user1.surname, 'zeSpychowa')
        self.assertEquals(self.user1.email, 'jurand@o.pl')
        self.assertEquals(self.user1.phone_number, '12343')
        self.assertEquals(self.user1.role, self.role1)
        usertest2 = User.objects.get(pk=2)
        self.assertNotEquals(usertest2.name, 'Jurand')

    def test_roles(self):
        self.assertEquals(self.role1.name, 'User')
        self.assertEquals(self.role2.name, 'Admin')

    def test_model_relation(self):
        self.assertEquals(self.role1.user_set.count(),2)
        self.assertNotEquals(self.role2.user_set.count(), 2)