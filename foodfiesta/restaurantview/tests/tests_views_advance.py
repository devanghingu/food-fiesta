from django.test import TestCase,RequestFactory
from django.contrib.auth.models import AnonymousUser,Group
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware
from django.urls            import reverse,resolve

from adminview.models      import City,Fooditem,Category
from accounts.models       import User
from restaurantview.models import Restaurant,Menu
from restaurantview.views import (AddNewRestaurant, Profile, ResturantDetailView,Home,MenuListView,AddFoodCreateView)

class CBVTestCaseMixin(TestCase):
    ''' Mixin of CBV Test Case '''
    view_class = None
    url        = None

    def _configure_for_session_message(self,request):
        # Add Session Middleware
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        # Add Message Middleware
        middleware = MessageMiddleware()
        middleware.process_request(request)
        request.session.save()
        
    def get_response(self, method, user, session, req_kwargs, args,kwargs):
        req_kwargs   = req_kwargs or {}
        request      = getattr(self.factory,method)(self.url,kwargs)
        request.user = user if user else AnonymousUser()
        # configure request with session and message framework
        self._configure_for_session_message(request)
        # Add Session if has
        if session:
            request.session = session
        return self.view_class.as_view()(request,**req_kwargs)

    
    def is_callable(self,user=None,post=False,session={},to=None,req_kwargs={},args=[],kwargs={}):
        post='post' if post else 'get'
        return self.get_response(user=user,method=post,session=session,req_kwargs=req_kwargs,args=args,kwargs=kwargs)


    

class CBVViewTestCase(CBVTestCaseMixin):

    def setUp(self):
        user_data         = {'first_name':'d2','last_name':'d2','username':'d2','email':'d2@gmail.com','password':'hello@123'}
        self.group        = Group.objects.create(name='staff_group')
        self.user         = User.objects.create_user(**user_data)
        self.user.groups.add(self.group)
        self.city         = City.objects.create(name='Bhavnagar')
        self.restaurant   = Restaurant.objects.create(user=self.user,name='New Resto',city=self.city,address='bhavnagar',contact='9574743817',active=True)
        self.assertTrue(self.restaurant)
        self.assertTrue(self.user)
        self.factory      = RequestFactory()

    def test_create_addnewrestaurant_POST(self):
        self.view_class = AddNewRestaurant
        self.url        = reverse('restaurantview:addnewrestaurant')
        data            = {'name':'New Name','address':'bhavnagar','city':self.city.pk,'contact':7545857501,'pic':''}
        response        = self.is_callable(user=self.user,post=True,kwargs=data)
        self.assertEqual(Restaurant.objects.last().name,data.get('name',False))
        self.assertRedirects(response,reverse('restaurantview:selectdashboard'),fetch_redirect_response=False)
      
    def test_detail_profile_GET(self):
        self.view_class     = Profile
        self.url            = resolve('/restaurant/profile')     
        session             = {'restaurant':self.restaurant.id}
        response            = self.is_callable(user=self.user,session=session)
        self.assertEqual(response.status_code,200)

    def test_restaurantdetail_GET(self):
        self.view_class     = ResturantDetailView
        self.url            = reverse('restaurantview:restaurantdetail',kwargs={'pk':self.restaurant.id})
        response            = self.is_callable(user=self.user,req_kwargs={'pk':self.restaurant.id})
        self.assertEqual(response.status_code,200)

    def test_home_GET(self):
        self.view_class     = Home
        self.url            = resolve('/restaurant/home')
        response            = self.is_callable(user=self.user)
        self.assertEqual(response.status_code,200)

    def test_menulistview_GET(self):
        self.view_class     = MenuListView
        self.url            = resolve('/restaurant/menu')
        response            = self.is_callable(user=self.user)
        self.assertIn('object_list',response.context_data)
        self.assertEqual(response.status_code,200)

    def test_addfoodcreateview_GET(self):
        self.view_class     = AddFoodCreateView
        self.url            = resolve('/restaurant/addfood')
        cat                 = Category.objects.create(name='veg')
        food                = Fooditem.objects.create(category=cat,name='name')
        data                = {'fooditem':food.pk,'price':130}
        session             = {'restaurant':self.restaurant.id}
        response            = self.is_callable(user=self.user,post=True,kwargs=data,session=session)  
        # print(response.url)
        self.assertEqual(Menu.objects.last().price,data.get('price',False))
        self.assertRedirects(response,expected_url='/restaurant/menu',status_code=302,target_status_code=200,fetch_redirect_response=False)