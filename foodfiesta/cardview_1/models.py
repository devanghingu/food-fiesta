from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User, Address
from restaurantview.models import Restaurant
from adminview.models import Fooditem


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    date = models.DateTimeField()
    total_price = models.PositiveIntegerField(default=0)
    status = models.SmallIntegerField(default=0)
    # delivery=models.OneToOneField(,on_delete=models.CASCADE)
    delivery_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user) + ' ' + str(self.restaurant) + str(self.total_price)


class Orderitem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Fooditem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return str(self.order) + str(self.food)