from django.urls import path
from django.conf.urls import url
from restaurantview.views import (Home,Profile,Invoice,
                                OrderPlacedListView,OrderAcceptedListView,ChangeOrderStatus,OrderRejectedListView,OrderDeliveredListView,
                                MenuListView,AddFoodCreateView,FoodDetailView,DeleteFoodDeleteView,
                                EditFoodDeleteView,AddFoodItemCreateView,
                                AddRestaurantCreateView,DeleteRestaurantDeleteView,DashBoard,
                                RestaurantList,EditRestaurantUpdateView,ResturantDetailView,ChangeStatus,
                                Customer,DeliveryList,AddDeliveryPersonCreateView,DeliveryDetailView)

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
    path('<int:pk>/<int:change_to>/changeorderstatus',ChangeOrderStatus.as_view(),name='changeorderstatus'),
    path('orderplaced',OrderPlacedListView.as_view(),name='orderplaced'),
    path('orderaccepted',OrderAcceptedListView.as_view(),name='orderaccepted'),
    path('orderrejected',OrderRejectedListView.as_view(),name='orderrejected'),
    path('orderdelivered',OrderDeliveredListView.as_view(),name='orderdelivered'),
  

    #invoice 
    path('<int:pk>/invoice',Invoice.as_view(),name='invoice'),

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
    path('delivery',DeliveryList.as_view(),name='delivery'),
    path('adddelivery',AddDeliveryPersonCreateView.as_view(),name='adddelivery'),
    path('<int:pk>/deliverydetail',DeliveryDetailView.as_view(),name='deliverydetail'),
]