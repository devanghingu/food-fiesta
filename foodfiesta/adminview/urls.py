from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required,user_passes_test

app_name = 'adminview'

urlpatterns = [
    path('index/', views.home,name='adminview_home'),
    #Category
    path('category/<int:pk>/', user_passes_test(lambda u: u.is_superuser)(views.CategoryDetail.as_view()), name='category_detail'),
    path('category/<int:pk>/update',user_passes_test(lambda u: u.is_superuser)(views.CategoryUpdate.as_view()),name='category_update'),
    path('category/<int:pk>/delete',user_passes_test(lambda u: u.is_superuser)(views.CategoryDelete.as_view()),name='category_delete'),
    path('categorylist/',user_passes_test(lambda u: u.is_superuser)(views.CategoryList.as_view()),name='allcategory'),
    path('category/create/',user_passes_test(lambda u: u.is_superuser)(views.CategoryCreate.as_view()),name='category_create'),
    #FoodItem
    path('fooditem/<int:pk>/', user_passes_test(lambda u: u.is_superuser)(views.FoodItemDetail.as_view()), name='fooditem_detail'),
    path('fooditem/<int:pk>/update',user_passes_test(lambda u: u.is_superuser)(views.FoodItemUpdate.as_view()),name='fooditem_update'),
    path('fooditem/<int:pk>/delete',user_passes_test(lambda u: u.is_superuser)(views.FoodItemDelete.as_view()),name='fooditem_delete'),
    path('fooditemlist/',user_passes_test(lambda u: u.is_superuser)(views.FoodItemList.as_view()),name='allfooditem'),
    path('fooditem/create/',user_passes_test(lambda u: u.is_superuser)(views.FoodItemCreate.as_view()),name='fooditem_create'),
    #City
    path('citylist/',user_passes_test(lambda u: u.is_superuser)(views.CityList.as_view()),name='allcity'),
    path('city/create/',user_passes_test(lambda u: u.is_superuser)(views.CityCreate.as_view()),name='city_create'),
    path('city/<int:pk>/update',user_passes_test(lambda u: u.is_superuser)(views.CityUpdate.as_view()),name='city_update'),
    path('city/<int:pk>/delete',user_passes_test(lambda u: u.is_superuser)(views.CityDelete.as_view()),name='city_delete'),
    #Restaurant
    path('restaurantlist/',user_passes_test(lambda u: u.is_superuser)(views.RestaurantList.as_view()),name='allrestaurant'),
    path('cancelrestaurantlist/',user_passes_test(lambda u: u.is_superuser)(views.Cancelequest.as_view()),name='cancelrestaurant'),
    path('restaurant/<int:id>/acceptrequest',views.Acceptrequest.as_view(),name='acceptrequest'),
    path('cancelrestaurant/<int:id>/acceptrequest',views.AcceptCancelrequest.as_view(),name='acceptcancelrequest'),
    path('cancelrestaurant/<int:id>/rejectrequest',views.Rejectrequest.as_view(),name='rejectrequest'),
    #Orders
    path('allorders/',user_passes_test(lambda u: u.is_superuser)(views.AllOrders.as_view()),name='allorders'),
    path('orderdetails/<int:pk>/',user_passes_test(lambda u: u.is_superuser)(views.OrderDetails.as_view()),name='orderdetails'),
    #Delivery
    path('deliverylist/',user_passes_test(lambda u: u.is_superuser)(views.DeliveryList.as_view()),name='deliverylist'),
    #Customer
    path('customerlist/',user_passes_test(lambda u: u.is_superuser)(views.AllCustomers.as_view()),name='customerlist'),
]
