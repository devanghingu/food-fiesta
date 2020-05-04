from django.test import TestCase
from .models import Restaurant
from  accounts.models import User
from  adminview.models import City
from foodfiesta.constants import OPEN,CLOSE,ACTIVE,DEACTIVE
# Create your tests here.

class   RestaurantModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='user')      
        self.city = City.objects.create(name='Ahmedabad')
        self.res =Restaurant.objects.create(user=self.user,name='New Resto',city=self.city)

    def test_resto_name(self):
        self.assertEqual(self.res.name,'New Resto')

    def test_resto_active(self):
        res = Restaurant.objects.create(name='New Resto',user=self.user,city=self.city,active=ACTIVE)
        self.assertTrue(res.active==ACTIVE,'Restaurant not active right now')

    def test_resto_open(self):
        res = Restaurant.objects.create(name='New Resto',user=self.user,city=self.city,open=CLOSE)
        self.assertFalse(res.open!=CLOSE,'Restaurant not open yet')


    