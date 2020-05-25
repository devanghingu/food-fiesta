from django.test import TestCase
from restaurantview.forms import DeliveryPersonForm
from foodfiesta.constants import AVAILABLE,NOT_AVAILABLE
from restaurantview.models import Restaurant,Delivery
from accounts.models    import User

class DeliveryPersonFormTestCase(TestCase):

    def test_valid_form(self):
        first_name = 'd2'
        last_name  = 'd2'
        username   = 'd2'
        email      = 'd2@gmail.com'
        password1  = 'hello@123'
        password2  = 'hello@123'
        user  = User(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
        data={'firstname':first_name,
            'last_name':last_name,
            'username':username,
            'email':email,
            'password1':password1,
            'password2':password2}
        form  = DeliveryPersonForm(data=data)    
        self.assertTrue(form.is_valid())
        print(form.errors)
        self.assertEqual(form.cleaned_data.get('username'),user.username)
        self.assertEqual(form.cleaned_data.get('password2'),user.password)

    def test_invalid_form(self):
        first_name = 'd2'
        last_name  = 'd2'
        username   = 'd2'
        email      = 'd2@gmail.com'
        password1  = 'hello@123'
        password2  = 'hello@1243'
        user  = User(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
        data={'firstname':first_name,
            'last_name':last_name,
            'username':username,
            'email':email,
            'password1':password1,
            'password2':password2}
        form  = DeliveryPersonForm(data=data)    
        self.assertFalse(form.is_valid())
        # print(form.errors)