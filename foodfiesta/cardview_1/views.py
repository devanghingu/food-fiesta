from django.shortcuts import render

# Create your views here.
from django.views import View


class RestaurantList(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'frontend/cardview/restaurantlist.html')

    def post(self, request, *args, **kwargs):
        pass


class RestaurantDetail(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'frontend/cardview/restaurant-detail.html')

    def post(self, request, *args, **kwargs):
        pass
