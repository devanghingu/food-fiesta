from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from restaurantview.models import Restaurant
from .models import Order, Orderitem
from adminview.models import Fooditem
from foodfiesta.constants import PENDING, ORDER_STATUS
from django.views import View


# Create your views here.

class cart(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'frontend/user_cart.html')

    def post(self, request, *args, **kwargs):
        pass


class restaurant(View):
    def get(self, request, *args, **kwargs):
        context = {}
        rest = Restaurant.objects.filter(id=kwargs['rest_id'])
        if rest.exists():
            context['restaurant'] = rest = rest.get()
            return render(request, 'frontend/user_restaurant.html', context)
        else:
            return render(request, 'frontend/404.html')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            cart = self.get_user_item_from_cart(request)  # checking items on cart
            rest_online = self.check_restaurant_online(request)
            if cart:
                pass
            else:
                # when cart is empty
                if rest_online:
                    pass  # if restaurnat online then check food item available
                    food_item = rest_online.fooditem.filter(id=request.POST.get('food_id'), available=True)
                    if food_item.exists():
                        pass
                    else:
                        pass

                else:
                    return JsonResponse(status=200, data={'message': 'Opps..!! Restaurant is offline currently.'})

        return JsonResponse(status=200, data={})

    def check_restaurant_online(self, request, *args, **kwargs):
        rest_online = Restaurant.objects.filter(id=request.POST.get('rest_id'), open=True)
        if rest_online.exists():
            return rest_online.get()
        return False  # when restaurant offline

    def get_user_item_from_cart(self, request, *args, **kwargs):
        userid = User.objects.get(id=3)  # static userid for kalpesh
        cart = Order.objects.filter(user=userid, status=PANDING)
        if cart.exists():
            return cart.get()
        return False


class AddToCart(View):
    pass
    # get_user_item_from_cart() # for check item on cart
    # check_same_item_not_in_cart()
    # check_restaurnt_is_online()
    # check_item_of_restaurnat_available()
