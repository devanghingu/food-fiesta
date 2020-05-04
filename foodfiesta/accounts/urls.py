from django.urls import path,include
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('',views.Index.as_view(),name='index'),
    path('createrestaurant',views.CreateRestaurant.as_view(),name='createrestaurant'),
]