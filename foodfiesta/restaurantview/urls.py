from django.urls import path
from django.conf.urls import url
from restaurantview.views import Home,Profile,Menu,AddFood,FoodDetail,Order,Invoice

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
]


