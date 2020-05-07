from django.urls import path

from . import views

app_name = 'cardview'
urlpatterns = [
    path('', views.RestaurantList.as_view(), name='res-list'),
    path('ajax_calls/search/', views.autocompletecity)
]
