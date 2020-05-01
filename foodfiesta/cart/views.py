from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from foodfiesta.constants import PENDING, ORDER_STATUS  
from django.views import View

from accounts.models import User,Address
from restaurantview.models import Restaurant
from .models import Order,Orderitem
from adminview.models import Fooditem
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
            context['cartitem']=[i.menu_id for i in Order.objects.get_user_item_from_cart(2).orderitem_set.all()]
            return render(request,'frontend/user_restaurant.html',context)

        return render(request,'frontend/404.html')
    
    def post(self,request,*args, **kwargs):
        user_id=2
        if request.is_ajax():
            cart        =   Order.objects.get_user_item_from_cart(user_id) # get user item from cart
            rest_online =   Restaurant.objects.check_restaurent_online(request.POST.get('rest_id'))
            if rest_online:
                if rest_online.menu_set.filter(id=request.POST.get('food_id'),available=True): #item available
                    if cart: #when cart is available      
                        if int(cart.restaurant_id) == int(request.POST.get('rest_id')):  
                            item    =   Orderitem.objects.add_item(cart,request.POST.get('food_id'))
                            if item:
                                total_item=cart.orderitem_set.count()
                                return JsonResponse(status=201,data={'message':'item added in cart','total_item':total_item})
                            return JsonResponse(status=201,data={'message':'item already in cart'})
                        else:
                            cart.delete()
                    cart    =   Order.objects.create_cart_object(user_id,rest_online)
                    item    =   Orderitem.objects.add_item(cart,request.POST.get('food_id'))
                    
                    total_item=cart.orderitem_set.count()
                    return JsonResponse(status=201,data={'message':'item added in cart','total_item':total_item}) 
                return JsonResponse(status=200,data={'message':'item not available at moment'})
            return JsonResponse(status=200,data={'message':'Opps..!! Restaurant is offline currently.'})

class AddToCart(View):
    pass