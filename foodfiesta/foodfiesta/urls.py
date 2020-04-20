from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('restaurant/',include('restaurantview.urls')),
    path('admin/', admin.site.urls),
]
