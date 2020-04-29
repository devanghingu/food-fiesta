from django.urls import path
from django.conf.urls import url
from restaurantview.views import (Home,Profile,Order,Invoice,
                                MenuListView,AddFoodCreateView,FoodDetailView,DeleteFoodDeleteView,
                                EditFoodDeleteView,AddFoodItemCreateView,
                                AddRestaurantCreateView,DeleteRestaurantDeleteView,DashBoard,
                                RestaurantList,EditRestaurantUpdateView,ResturantDetailView,ChangeStatus,
                                Customer,Delivery)

app_name = 'restaurantview'
urlpatterns = [
    path('home',Home.as_view(),name='home'),
    path('profile',Profile.as_view(),name='profile'),

    #menu
    path('menu',MenuListView.as_view(),name='menu'),
    path('addfood',AddFoodCreateView.as_view(),name='addfood'),
    path('<int:pk>/fooddetail',FoodDetailView.as_view(),name='fooddetail'),
    path('<int:pk>/editfood',EditFoodDeleteView.as_view(),name='editfood'),
    path('<int:pk>/deletefood',DeleteFoodDeleteView.as_view(),name='deletefood'),

    #add FoodItem
    path('addfooditem',AddFoodItemCreateView.as_view(),name='addfooditem'),

    #order
    path('order',Order.as_view(),name='order'),

    #invoice 
    path('invoice',Invoice.as_view(),name='invoice'),

    #restaurant
    path('restaurant',RestaurantList.as_view(),name='restaurant'),
    path('addrestaurant',AddRestaurantCreateView.as_view(),name='addrestaurant'),
    path('<int:pk>/editrestaurant',EditRestaurantUpdateView.as_view(),name='editrestaurant'),
    path('<int:pk>/deleterestaurant',DeleteRestaurantDeleteView.as_view(),name='deleterestaurant'),
    path('<int:pk>/restaurantdetail',ResturantDetailView.as_view(),name='restaurantdetail'),
    path('status',ChangeStatus.as_view(),name='status'),
    path('<int:pk>/dashboard',DashBoard.as_view(),name='dashboard'),

    #customer
    path('customer',Customer.as_view(),name='customer'),

    #delivery person
    path('delivery',Delivery.as_view(),name='delivery'),
]