from django.shortcuts import render

# Create your views here.
from django.views import View


class cart(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'frontend/cardview/restaurantlist.html')

    def post(self, request, *args, **kwargs):
        pass
