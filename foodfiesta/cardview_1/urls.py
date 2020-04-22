from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.RestaurantList.as_view(), name='cardview'),
    path('restaurant/detail',views.RestaurantDetail.as_view(),name='res-detail')
]
