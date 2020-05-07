from django.shortcuts import render
from django.views import View


class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'backend/restaurantview/index.html')


class Profile(View):
    def get(self, request, *args, **kwargs):
        return render(request,
                      'backend/restaurantview/pages/product/restaurant-profile.html')


class Menu(View):
    def get(self, request, *args, **kwargs):
        return render(request,
                      'backend/restaurantview/pages/product/foodgrid.html')


class AddFood(View):
    def get(self, request, *args, **kwargs):
        return render(request,
                      'backend/restaurantview/pages/product/addfood.html')


class FoodDetail(View):
    def get(self, request, *args, **kwargs):
        return render(request,
                      'backend/restaurantview/pages/product/fooddetail.html')


class Order(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'backend/restaurantview/pages/orders.html')


class Invoice(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'backend/restaurantview/pages/invoice.html')
