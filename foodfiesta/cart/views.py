from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView
from restaurantview.models import Restaurant
from .models import Order, Orderitem
from adminview.models import Fooditem
from foodfiesta.constants import PENDING, ORDER_STATUS, PLACED
from django.views import View


# Create your views here.


class cart(View):
    def get(self, request, *args, **kwargs):
        rest_id = 2
        ordr = get_object_or_404(Order, user__id=2, restaurant__id=rest_id, status=0)
        cartitem = Orderitem.objects.filter(order=ordr).order_by('id')
        amount = sum([item.price for item in cartitem])
        return render(request, 'frontend/user_cart.html', {'cartitem': cartitem, 'amount': amount, 'rest_id': rest_id})

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
            cart = Order.objects.get_user_item_from_cart('3')  # get user item from cart
            rest_online = Restaurant.objects.check_restaurent_online(request.POST.get('rest_id'))
            if cart:
                pass
            else:
                # when cart is empty
                if rest_online:
                    food_item = rest_online.fooditem.filter(id=request.POST.get('food_id'), available=True)
                    if food_item.exists():
                        pass
                        # create cart
                    else:
                        pass

                else:
                    return JsonResponse(status=200, data={'message': 'Opps..!! Restaurant is offline currently.'})
        return JsonResponse(status=200, data={})


class AddToCart(View):
    pass
    # get_user_item_from_cart() # for check item on cart
    # check_same_item_not_in_cart()
    # check_restaurnt_is_online()
    # check_item_of_restaurnat_available()


def modify_quantity(request):
    qty = request.GET.get('qty', None)
    orditm_id = request.GET.get('orditm_id', None)
    proposed_orderitem = Orderitem.objects.get(id=orditm_id)
    old_price = proposed_orderitem.price
    proposed_orderitem.quantity = qty
    proposed_orderitem.price = int(qty) * int(proposed_orderitem.menu.price)
    proposed_orderitem.save()
    order_id = proposed_orderitem.id
    print('old_price:', old_price)
    print('new_price:', proposed_orderitem.price)
    price_adj = proposed_orderitem.price - old_price
    # if old_price > proposed_orderitem.price:
    #     price_adj = -price_adj
    print(price_adj)
    data = {
        'order_id': order_id,
        'price_adj': price_adj
    }
    return JsonResponse(status=200, data=data)


class CartItemDelete(DeleteView):
    model = Orderitem
    success_url = reverse_lazy('cart:cart')

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        res = self.object.order.restaurant
        print(res.id)
        order = Order.objects.get(restaurant=res, user__id=2).orderitem_set.all()
        if not order:
            Order.objects.get(restaurant=res, user__id=2).delete()
            return redirect(request, 'cart:restaurant', {'rest_id': res.id})
        return HttpResponseRedirect(success_url)


def placeorder(request, rest_id):
    usr = 2
    order = Order.objects.get(user__id=usr, restaurant__id=rest_id)
    order.status = PLACED
    order.save()
    messages.success(request,'Your order has been Placed!..')
    object_list = Order.objects.filter(user__id=2)
    return render(request, 'frontend/myorderlist.html', {'object_list': object_list})


class OrderList(ListView):
    model = Order
    template_name = 'frontend/myorderlist.html'

    # paginate_by = 100  # if pagination is desired

    def get_queryset(self):
        return Order.objects.filter(user__id=2)
