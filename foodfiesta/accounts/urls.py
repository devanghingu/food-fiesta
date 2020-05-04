from accounts import views
from django.urls import include, path

app_name = "accounts"

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("createrestaurant", views.CreateRestaurant.as_view(), name="createrestaurant"),
]
