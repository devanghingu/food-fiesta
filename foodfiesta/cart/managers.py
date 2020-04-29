from django.db import models
from foodfiesta.constants import PENDING, ORDER_STATUS
from django.contrib.auth.models import User 
class OrderManager(models.Manager):
    def get_user_item_from_cart(self,user_id):
        userid=User.objects.get(id=3) #static userid for kalpesh
        cart=Order.objects.filter(user=userid,status=PANDING)
        if cart.exists():
            return cart.get()
        return False