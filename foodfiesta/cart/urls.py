from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('cart',views.cart.as_view(),name='cart')
]