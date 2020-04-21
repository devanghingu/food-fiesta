from django.urls import path,include
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('',views.Index.as_view(),name='index'),
]