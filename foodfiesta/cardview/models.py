from django.db import models
from accounts.models import User
from restaurantview.models import Restaurant,Delivery
from adminview.models import Fooditem
from accounts.models import Address
from foodfiesta.constants import ORDER_STATES

class Order(models.Model):
    user            = models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant      = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    address         = models.ForeignKey(Address,on_delete=models.CASCADE)
    date            = models.DateTimeField()
    total_price     = models.PositiveIntegerField()
    status          = models.SmallIntegerField(choices=ORDER_STATES)
    delivery        = models.ForeignKey(Delivery,on_delete=models.CASCADE)

    def __str__(self):
        return self.restaurant
    
class Orderitem(models.Model):
    order       = models.ForeignKey(Order,on_delete=models.CASCADE)
    food        = models.ForeignKey(Fooditem,on_delete=models.CASCADE)
    quantity    = models.PositiveIntegerField()
    price       = models.PositiveIntegerField()

    def __str__(self):
        return self.id
