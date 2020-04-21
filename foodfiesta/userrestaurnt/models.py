from django.db import models

from .constants import STATUS,PANDING
class Order(models.Model):
    """  """
    date            = models.DateTimeField()
    total_price     = models.PositiveIntegerField()
    status          = models.SmallIntegerField(choices=STATUS,default=PANDING)
    restaurant      = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    # address         = models.ForeignKey(Address,on_delete=models.CASCADE)
    # user            = models.ForeignKey(User,on_delete=models.CASCADE)
    # delivery        =models.OneToOneField()
    # delivery_status =models.BooleanField()

#Order
class Orderitem(models.Model):
    order       = models.ForeignKey(Order,on_delete=models.CASCADE)
    food        = models.ForeignKey(Fooditem,on_delete=models.CASCADE)
    quantity    = models.PositiveIntegerField()
    price       = models.PositiveIntegerField()
class Fooditem(models.Model):
    # category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=75)
    description=models.TextField()
    pic=models.ImageField(upload_to='fooditem/')

class Restaurant(models.Model):
    name    =models.CharField(max_length=75)
    contact =models.CharField(max_length=13)
    address =models.TextField(max_length=255)
    open    =models.BooleanField(default=False)
    active  =models.BooleanField(default=False)
    pic     =models.ImageField(upload_to='restaurant/')
    # city    =models.ForeignKey(City,on_delete=models.CASCADE)
    # user    =models.ForeignKey(User,on_delete=models.CASCADE)
    parent  =models.ForeignKey('Restaurant',on_delete=models.CASCADE)
    # fooditem=models.ManyToManyField(Fooditem)


class City(models.Model):
    name        =models.CharField(max_length=255)
    description =models.TextField()
