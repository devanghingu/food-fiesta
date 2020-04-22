from django.shortcuts import render

# Create your views here.
from django.views import View

from restaurantview.models import Restaurant


class RestaurantList(View):
    def get(self, request, *args, **kwargs):
        # res_list = Restaurant.objects.all()
        return render(request, 'frontend/cardview/restaurantlist.html',{'res_list':res_list})

    def post(self, request):
        searchinput = request.POST.get('')

