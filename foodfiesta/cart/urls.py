from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "cart"
urlpatterns = [
    path('cart', views.cart.as_view(), name='cart'),
    path('addtocart', views.cart.as_view(), name='addtocart'),
    path('restaurant/<int:rest_id>', views.restaurant.as_view(), name='restaurant'),
    path('modify/quantity/', views.modify_quantity, name='addtocart'),
    path('remove/item/<int:pk>/', views.CartItemDelete.as_view(), name='item-remove'),
    path('order/placed/<int:rest_id>/', views.placeorder, name='placed-order'),
    path('myorder-list/',views.OrderList.as_view(),name='myorder-list'),
]
