from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView
from restaurantview.models import Restaurant
from .models import Order, Orderitem
from foodfiesta.constants import PENDING, ORDER_STATUS, PLACED
from django.views import View


# Create your views here.

class cart(View):
    def get(self, request, *args, **kwargs):
        print(request.user)
        try:
            ordr = get_object_or_404(Order, user=request.user, status=0)
        except:
            ordr = None
        cartitem = Orderitem.objects.filter(order=ordr).order_by('id')
        amount = sum([item.price for item in cartitem])
        return render(request, 'frontend/user_cart.html', {'cartitem': cartitem, 'amount': amount})

    def post(self, request, *args, **kwargs):
        pass


class restaurant(View):
    def get(self, request, *args, **kwargs):
        context = {}
        rest = Restaurant.objects.filter(id=kwargs['rest_id'])
        if rest.exists():
            context['restaurant'] = rest = rest.get()
            context['cartitem'] = [
                i.menu_id for i in Order.objects.get_user_item_from_cart(2).orderitem_set.all()]
            return render(request, 'frontend/user_restaurant.html', context)

        return render(request, 'frontend/404.html')

    def post(self, request, *args, **kwargs):
        user_id = 2
        if request.is_ajax():
            cart = Order.objects.get_user_item_from_cart(
                user_id)  # get user item from cart
            rest_online = Restaurant.objects.check_restaurent_online(
                request.POST.get('rest_id'))
            if rest_online:
                # item available
                if rest_online.menu_set.filter(id=request.POST.get('food_id'), available=True):
                    if cart:  # when cart is available
                        if int(cart.restaurant_id) == int(request.POST.get('rest_id')):
                            item = Orderitem.objects.add_item(
                                cart, request.POST.get('food_id'))
                            if item:
                                total_item = cart.orderitem_set.count()
                                return JsonResponse(status=201,
                                                    data={'message': 'item added in cart', 'total_item': total_item})
                            return JsonResponse(status=201, data={'message': 'item already in cart'})
                        else:
                            cart.delete()
                    cart = Order.objects.create_cart_object(
                        user_id, rest_online)
                    item = Orderitem.objects.add_item(
                        cart, request.POST.get('food_id'))

                    total_item = cart.orderitem_set.count()
                    return JsonResponse(status=201, data={'message': 'item added in cart', 'total_item': total_item})
                return JsonResponse(status=200, data={'message': 'item not available at moment'})
            return JsonResponse(status=200, data={'message': 'Opps..!! Restaurant is offline currently.'})


def modify_quantity(request):
    qty = request.GET.get('qty', None)
    orditm_id = request.GET.get('orditm_id', None)
    proposed_orderitem = Orderitem.objects.get(id=orditm_id)
    old_price = proposed_orderitem.price
    proposed_orderitem.quantity = qty
    proposed_orderitem.price = int(qty) * int(proposed_orderitem.menu.price)
    proposed_orderitem.save()
    order_id = proposed_orderitem.id
    price_adj = proposed_orderitem.price - old_price
    # if old_price > proposed_orderitem.price:
    #     price_adj = -price_adj
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
        res_id = self.object.order.restaurant.id
        print(res_id)
        order = Order.objects.get(user=request.user).orderitem_set.all()
        if not order:
            Order.objects.get(user=request.user).delete()
            return redirect('cart:restaurant', rest_id=res_id)
        return HttpResponseRedirect(success_url)


def placeorder(request):
    order = Order.objects.get(user=request.user)
    order.status = PLACED
    order.save()
    messages.success(request, 'Your order has been Placed!..')
    object_list = Order.objects.filter(user=request.user)
    return render(request, 'frontend/myorderlist.html', {'object_list': object_list})


class OrderList(ListView):
    model = Order
    template_name = 'frontend/myorderlist.html'

    # paginate_by = 100  # if pagination is desired

    def get_queryset(self):
        return Order.objects.filter(user=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super(OrderList, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
