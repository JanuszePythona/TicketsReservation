from django.test import TestCase
from Login.models import User,Role
from django.core.urlresolvers import reverse
from django.core.urlresolvers import resolve


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
        self.assertNotEquals(Role.objects.get(pk=2).name, self.role1.name)

    def test_model_relation(self):
        self.assertEquals(self.role1.user_set.count(),2)
        self.assertNotEquals(self.role2.user_set.count(), 2)

    def test_roles_str(self):
        role = Role.objects.get(pk=1)
        self.assertEqual(str(role), role.name)

    def test_user_str(self):
        user = User.objects.get(pk=1)
        self.assertEqual(str(user), user.name)

    def test_urls_names(self):
        url = reverse('register')
        self.assertEqual(url, '/register/')
        url = reverse('login')
        self.assertEqual(url, '/login/')
        url = reverse('logout')
        self.assertEqual(url, '/logout/')

    def test_url_connect_to_view(self):
        resolver = resolve('/register/')
        self.assertEqual(resolver.view_name, 'register')
        resolver = resolve('/login/')
        self.assertEqual(resolver.view_name, 'login')
        resolver = resolve('/logout/')
        self.assertEqual(resolver.view_name, 'logout')