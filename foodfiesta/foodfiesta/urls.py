
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('cart.urls')),
    path('restaurant/',include('restaurantview.urls')),
    path('admin/', admin.site.urls),
    path('cardview/',include('cardview.urls')),
    path('adminview/',include('adminview.urls')),
]
