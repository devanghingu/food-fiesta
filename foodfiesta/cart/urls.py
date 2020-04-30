from django.contrib import admin
from django.urls import path,include
from . import views
app_name="cart"
urlpatterns = [
    path('cart',views.cart.as_view(),name='cart'),
    path('addtocart',views.cart.as_view(),name='addtocart'),
    path('restaurant/<int:rest_id>',views.restaurant.as_view(),name='restaurant')
]