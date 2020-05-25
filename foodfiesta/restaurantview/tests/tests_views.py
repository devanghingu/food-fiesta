from django.test import TestCase,RequestFactory 
from django.urls import reverse
from accounts.models import User
from django.contrib.auth.models import Group
from adminview.models import City
from restaurantview.views import Home

class RestaurantviewViewTestCase(TestCase):
    def setUp(self):
        first_name = 'd2'
        last_name  = 'd2'
        username   = 'd2'
        email      = 'd2@gmail.com'
        password1  = 'hello@123'
        # create group
        self.group,create = Group.objects.get_or_create(name='staff_group')
        # create user
        self.user  = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
        self.user.groups.add(self.group)
        
        
        self.assertTrue(self.user)
        self.factory = RequestFactory()
    
    # another way of do login using self.client 
    def do_login(self):
        return self.client.login(username='d2',password='hello@123')

    def test_home_GET(self):
        url          = reverse('restaurantview:home')
        login        = self.do_login()
        # first way of login using request factory through
        request      = self.factory.get(url)
        # login by assing
        request.user = self.user 

        self.assertTrue(login)
        #first way of use class base view
        response = Home.as_view()(request) 
        #second way"python.linting.pylintArgs": ["--disable","no-member"],
        view = Home()
        view = view.setup(request)
        # print(response.conext)        
        # self.assertIn('context attribute name',context)
        self.assertEqual(response.status_code,200)

    def test_selectdashboard_GET(self):
        url      = reverse('restaurantview:selectdashboard') 
        login   = self.do_login()
        self.assertTrue(login)
        response = self.client.get(url)
        self.assertIn('object_list',response.context)
        self.assertEqual(response.status_code,200)
        # print(response.get('location'))

    # def test_addnewrestaurant_POST(self):
    #     url         = reverse('restaurantview:addnewrestaurant')
    #     city,create = City.objects.get_or_create(name='Bhavnagar')
    #     data        = {'name':'New Resto','address':'bhavnagar','city':city,'contact':7545857501,'pic':''}
    #     login       = self.do_login()
    #     response = self.client.post(url,data=data)
    #     self.assertEqual(response.status_code,200)
    #     # print(response.get('location'))