from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from restaurantview.models import Restaurant
from .models import Order,Orderitem
from adminview.models import Fooditem
from foodfiesta.constants import PENDING, ORDER_STATUS  
from django.views import View
# Create your views here.

class cart(View):
    def get(self,request,*args, **kwargs):
        return render(request,'frontend/user_cart.html')
    def post(self,request,*args, **kwargs):
        pass

class restaurant(View):
    def get(self,request,*args, **kwargs):
        context={}
        rest=Restaurant.objects.filter(id=kwargs['rest_id'])
        if rest.exists():
            context['restaurant']=rest=rest.get()   
            return render(request,'frontend/user_restaurant.html',context)
        else:
            return render(request,'frontend/404.html')
    
    def post(self,request,*args, **kwargs):

        if request.is_ajax():
            cart=Order.objects.get_user_item_from_cart('3') # get user item from cart
            rest_online=Restaurant.objects.check_restaurent_online(request.POST.get('rest_id'))
            if cart:
                pass
            else:
                # when cart is empty
                if rest_online:
                    food_item=rest_online.fooditem.filter(id=request.POST.get('food_id'),available=True)
                    if food_item.exists():
                        pass
                        # create cart
                    else:
                        pass

                else:
                    return JsonResponse(status=200,data={'message':'Opps..!! Restaurant is offline currently.'})
        return JsonResponse(status=200,data={})

class AddToCart(View):
    pass
    # get_user_item_from_cart() # for check item on cart
    # check_same_item_not_in_cart()
    # check_restaurnt_is_online()
    # check_item_of_restaurnat_available()
        
