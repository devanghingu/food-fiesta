from accounts import views
from django.urls import include
from django.urls import path

app_name = "accounts"

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("createrestaurant",
         views.CreateRestaurant.as_view(),
         name="createrestaurant"),
]
