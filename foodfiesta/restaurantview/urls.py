from django.urls import path
from django.conf.urls import url
from restaurantview.views import (Home,Profile,Menu,AddFood,FoodDetail,Order,
                                  Invoice,Restaurant,EditRestaurant,RestaurantDetail,
                                  Customer,Delivery)

app_name = 'restaurantview'
urlpatterns = [
    path('home',Home.as_view(),name='home'),
    path('profile',Profile.as_view(),name='profile'),

    #menu
    path('menu',Menu.as_view(),name='menu'),
    path('addfood',AddFood.as_view(),name='addfood'),
    path('fooddetail',FoodDetail.as_view(),name='fooddetail'),

    #order
    path('order',Order.as_view(),name='order'),

    #invoice 
    path('invoice',Invoice.as_view(),name='invoice'),

    #restaurant
    path('restaurant',Restaurant.as_view(),name='restaurant'),
    path('editrestaurant',EditRestaurant.as_view(),name='editrestaurant'),
    path('restaurantdetail',RestaurantDetail.as_view(),name='restaurantdetail'),

    #customer
    path('customer',Customer.as_view(),name='customer'),

    #delivery person
    path('delivery',Delivery.as_view(),name='delivery'),
]



