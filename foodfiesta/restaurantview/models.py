from django.db import models
from adminview.models import City,Fooditem
from accounts.models import User
from foodfiesta.constants import DELIVERY_STATUS,OPEN_STATUS,ACTIVE_STATUS

class Restaurant(models.Model):
    user        = models.ForeignKey(User,on_delete=models.CASCADE)
    parent      = models.ForeignKey('Restaurant',on_delete=models.CASCADE,blank=True,null=True)
    fooditem    = models.ManyToManyField(Fooditem,through='Menu')
    name        = models.CharField(max_length=75)
    address     = models.TextField(max_length=255)
    city        = models.ForeignKey(City,on_delete=models.CASCADE)
    contact     = models.CharField(max_length=13)
    open        = models.BooleanField(choices=OPEN_STATUS,default=False)
    active      = models.BooleanField(choices=ACTIVE_STATUS,default=False)
    pic         = models.ImageField(upload_to='restaurant/',blank=True,null=True)

    Restaurant = models.Manager()
    objects = RestaurantManager()

    def __str__(self):
        return self.name

class Menu(models.Model):
    fooditem    = models.ForeignKey(Fooditem,on_delete=models.CASCADE)
    restaurant  = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    price       = models.PositiveIntegerField(default=0)
    available   = models.BooleanField(default=False)

    def __str__(self):
        return self.fooditem.name

class Delivery(models.Model):
    user       = models.OneToOneField(User,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    status     = models.BooleanField(choices=DELIVERY_STATUS,default=False)

    def __str__(self):
        return self.user.username
