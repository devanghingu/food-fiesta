from django.urls import path
from django.conf.urls import url
from restaurantview.views import Home
urlpatterns = [
    path('home',Home.as_view(),name='home')
]
