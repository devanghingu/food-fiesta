from django.db import models
from accounts.models import User
from restaurantview.models import Restaurant,Delivery,Menu
from accounts.models import Address

from foodfiesta.constants import ORDER_STATUS,PENDING
from .managers import OrderManager
class Order(models.Model):
    user            = models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant      = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    address         = models.ForeignKey(Address,on_delete=models.CASCADE)
    date            = models.DateTimeField(auto_now_add=True)
    total_price     = models.PositiveIntegerField(default=True)
    status          = models.SmallIntegerField(choices=ORDER_STATUS, default=PENDING)
    delivery        = models.ForeignKey(Delivery,on_delete=models.CASCADE,null=True,blank=True)

    Order=models.Manager()
    objects= OrderManager()

    def __str__(self):
        return self.user.username
    
class Orderitem(models.Model):
    order       = models.ForeignKey(Order,on_delete=models.CASCADE)
    menu        = models.ForeignKey(Menu,on_delete=models.CASCADE,null=True,blank=True)
    quantity    = models.PositiveIntegerField()
    price       = models.PositiveIntegerField()

    def __str__(self):
        return str(self.order)