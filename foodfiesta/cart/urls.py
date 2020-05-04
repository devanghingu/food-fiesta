from django.contrib import admin
from django.urls import include
from django.urls import path

from . import views

app_name = "cart"
urlpatterns = [
    path("cart/", views.cart.as_view(), name="cart"),
    path("addtocart", views.cart.as_view(), name="addtocart"),
    path("restaurant/<int:rest_id>",
         views.restaurant.as_view(),
         name="restaurant"),
    path("modify/quantity/", views.modify_quantity, name="quantity"),
    path("remove/item/<int:pk>/",
         views.CartItemDelete.as_view(),
         name="item-remove"),
    path("order/placed/", views.placeorder, name="placed-order"),
    path("myorder-list/", views.OrderList.as_view(), name="myorder-list"),
]
