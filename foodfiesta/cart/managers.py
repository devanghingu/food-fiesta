from accounts.models import Address
from accounts.models import User
from django.db import models
from foodfiesta.constants import PENDING
from restaurantview.models import Menu


# from .models import Order
class OrderManager(models.Manager):
    def get_user_item_from_cart(self, user_id):
        user = User.objects.get(id=user_id)  # static userid for kalpesh
        cart = self.filter(user=user, status=PENDING)
        if cart.exists():
            return cart.get()
        return False

    def create_cart_object(self, user_id, restaurant):
        # userid, restuant_id,address
        # date,total_price( optinal) status,delivery optional
        address = Address.objects.get_user_address(user_id)
        if address:
            user = User.objects.get(id=user_id)
            cart = self.create(user=user, address=address,
                               restaurant=restaurant)
            return cart
        return False

    def order_total_price(self):
        return sum([self.orderitem_set.all()])

    def update_cart_object(self):
        pass

    def delete_cart_object(self):
        pass


class OrderitemManager(models.Manager):
    def add_item(self, order, item_id):

        menu = Menu.objects.get(id=item_id)  # get item from menu
        cartitem = self.filter(order=order)
        if cartitem.exists():
            if int(item_id) in [i.menu_id for i in cartitem]:
                return False
        return self.create(order=order, menu=menu, quantity=1,
                           price=menu.price)

    def remove_item(self, order, item_id):
        pass
