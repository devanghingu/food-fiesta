from django.urls import path

from . import views

app_name = 'adminview'

urlpatterns = [
    path('index/', views.home, name='adminview_home'),
]
